from enum import Enum

from main import redis_client


class Status(Enum):
    ACCEPTED = "Accepted"
    RUNNING = "Running"
    COMPLETE = "Complete"
    NOT_FOUND = "Not-Found"
    ERROR = "Error"



def update_crawl_status(crawl_id, status: Status, extra: str = None):
    redis_client.set(crawl_id, status.value)

def get_crawl_status(crawl_id) -> str:
    status = redis_client.get(crawl_id)
    return status

