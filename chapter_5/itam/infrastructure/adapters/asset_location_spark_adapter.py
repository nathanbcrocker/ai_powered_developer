from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, expr, udf
from pyspark.sql.types import StructType, StructField, IntegerType, DoubleType, TimestampType, FloatType
from geopy.distance import distance
import os

os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-10_2.12:3.2.0,org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0 pyspark-shell'

def calculate_distance(lat1, lon1, lat2, lon2):
    return distance((lat1, lon1), (lat2, lon2)).miles


class AssetLocationSparkAdapter:
    def __init__(self):
        self.schema = StructType([
            StructField("asset_id", IntegerType()),
            StructField("latitude", DoubleType()),
            StructField("longitude", DoubleType()),
            StructField("timestamp", TimestampType())
        ])

        # Create a SparkSession
        self.spark = SparkSession.builder \
            .appName("AssetLocationSparkAdapter") \
            .getOrCreate()
        
        self.spark.udf.register("calculate_distance", calculate_distance)

        # Create a streaming DataFrame from the asset_location topic
        self.df = self.spark \
            .readStream \
            .format("kafka") \
            .option("kafka.bootstrap.servers", "localhost:9092") \
            .option("subscribe", "asset_location") \
            .option("startingOffsets", "earliest") \
            .load() \
            .selectExpr("CAST(value AS STRING)")

        # Parse the incoming JSON data
        self.parsed_stream = self.df \
            .select(from_json(col("value"), self.schema).alias("data")) \
            .select("data.*")

        # Calculate the distance between the current location and Chicago for each asset
        self.distance = self.parsed_stream \
            .withColumn("distance", expr("calculate_distance(latitude, longitude, 41.8781, -87.6298)")) \
            .select(col("asset_id"), col("timestamp"), col("distance")) \
            .filter(col("distance") > 25)

        # Write the results to the console
        self.query = self.distance \
            .writeStream \
            .outputMode("append") \
            .format("console") \
            .start()

    def run(self):
        self.query.awaitTermination()

    def stop(self):
        # Stop the streaming query and SparkSession
        self.query.stop()
        self.spark.stop()