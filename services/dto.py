import datetime
from dataclasses import dataclass


@dataclass
class Weather:
    name: str
    temperature: float
    timestamp: datetime

    def __iter__(self):
        yield self.name
        yield self.temperature
        yield self.timestamp
