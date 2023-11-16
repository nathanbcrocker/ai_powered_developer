# Define a class called SnowflakeIdentifier
# It should generate an identifier using the snowflake algorithm
# Combine the current time in milliseconds since the epoch time (January 1, 2021 in this case) with the machine ID and sequence number to create the ID.
# The ID should be a 64-bit integer

import time
import uuid

class SnowflakeIdentifier:
    def __init__(self):
        self._machine_id = uuid.getnode()
        self._sequence_number = 0
        self._last_timestamp = 0

    def get_id(self):
        timestamp = int(time.time() * 1000)
        if timestamp == self._last_timestamp:
            self._sequence_number += 1
        else:
            self._sequence_number = 0
        self._last_timestamp = timestamp
        return (timestamp << 22) + (self._machine_id << 10) + self._sequence_number