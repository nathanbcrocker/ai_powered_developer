from kafka import KafkaConsumer
from itam.domain.events.asset_location_updated import AssetLocationUpdated
import json
import asyncio

class AssetLocationKafkaConsumer:
    def __init__(self, mediator):
        self.mediator = mediator

        self.consumer = KafkaConsumer(
            'asset_location',
            bootstrap_servers=['localhost:9092'],
            enable_auto_commit=True,
            group_id='itam-group',
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )

        # Define a function to process Kafka messages
    async def process_messages_async(self):
        for message in self.consumer:
            asset_id = message.value['asset_id']
            latitude = message.value['latitude']
            longitude = message.value['longitude']
            timestamp = message.value['timestamp']
            event = AssetLocationUpdated(asset_id, latitude, longitude, timestamp)
            self.mediator.publish(event)

    async def start_consumer_async(self):
        print('Starting Kafka consumer...') 
        await self.process_messages_async()

    def start_consumer(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.start_consumer_async())