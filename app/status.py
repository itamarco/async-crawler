from enum import Enum
import os
import redis

redis_host = os.environ.get('REDIS_HOST')
redis_client = redis.StrictRedis(host=redis_host, port=6379, db=0, decode_responses=True)


class Status(Enum):
    ACCEPTED = "Accepted"
    RUNNING = "Running"
    COMPLETE = "Complete"
    NOT_FOUND = "Not-Found"
    ERROR = "Error"


def update_crawl_status(crawl_id, status: Status, extra: str = None):
    redis_client.set(crawl_id, status.value)


def read_crawl_status(crawl_id) -> str:
    status = redis_client.get(crawl_id)
    return status
