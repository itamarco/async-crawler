from celery import Celery
import os

from app.crawler import crawl_url
from app.status import update_crawl_status, Status

redis_url = os.environ.get('REDIS_URL')

app = Celery('crawler', broker=redis_url)

@app.task
def crawl_web_page(url, crawl_id):
    update_crawl_status(crawl_id, Status.RUNNING)
    try:
        html = crawl_url(url)

    except Exception as e:
        update_crawl_status(crawl_id, Status.ERROR)
