import logging

from celery import Celery
import os

from utils import crawl_url, save_webpage
from status import update_crawl_status, Status

redis_url = os.environ.get('BROKER_URL')

app = Celery('crawler', broker=redis_url)

logger = logging.getLogger("worker")


@app.task
def crawl_web_page(url, crawl_id):
    logger.info(f"Start crawling {url} [{crawl_id}]")
    update_crawl_status(crawl_id, Status.RUNNING)
    try:
        html = crawl_url(url)
        save_webpage(crawl_id, html)
        update_crawl_status(crawl_id, Status.COMPLETE)
    except Exception as e:
        update_crawl_status(crawl_id, Status.ERROR)
        logger.exception(f"Failed to crawl {url} [{crawl_id}")
