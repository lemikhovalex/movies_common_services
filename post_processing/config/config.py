import os
from dataclasses import dataclass


@dataclass
class Config:
    es_host: str = os.getenv('ES_HOST', 'elasticsearch')
    es_port: str | int = os.getenv('ES_PORT', 9200)


CONFIG = Config()
