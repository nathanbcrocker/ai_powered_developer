# Importing the necessary modules and packages
# Instantiating the necessary objects and components, such as the FastAPI application and database connection
# Configuring the application settings and environment variables
# Mounting the HTTP controllers and endpoints to the FastAPI application
# Starting the server and running the application
from pyspark.sql import SparkSession
from fastapi import FastAPI
from itam.infrastructure.api.asset_controller import AssetController
#from itam.infrastructure.repository.in_memory_asset_repository import InMemoryAssetRepository
from itam.infrastructure.repository.sqlalchemy_asset_repository import SQLAlchemyAssetRepository
from itam.infrastructure.database.database_connection import DatabaseConnection
from itam.service.asset_manager import AssetManager 
from itam.infrastructure.mediators.asset_location_mediator import AssetLocationMediator
from itam.infrastructure.adapters.asset_rest_adapter import AssetRestAdapter
from itam.infrastructure.consumers.asset_location_kafka_consumer import AssetLocationKafkaConsumer
from itam.infrastructure.adapters.asset_location_spark_adapter import AssetLocationSparkAdapter
import uvicorn

app = FastAPI()
session = DatabaseConnection().get_session()
#repository = InMemoryAssetRepository()
repository = SQLAlchemyAssetRepository(session)
mediator = AssetLocationMediator()
asset_manager = AssetManager(repository, mediator)
asset_rest_adapter = AssetRestAdapter(asset_manager)
asset_controller = AssetController(asset_rest_adapter)

app.include_router(asset_controller.get_router())

#consumer = AssetLocationKafkaConsumer(mediator)
#consumer.start_consumer()

#spark_adapter = AssetLocationSparkAdapter()
#spark_adapter.run()
app.include_router(asset_controller.get_router())

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)