from celery import Celery
import os

from crawler import crawl_url
from status import update_crawl_status, Status
from webpage import save_webpage

redis_url = os.environ.get('BROKER_URL')

app = Celery('crawler', broker=redis_url)


@app.task
def crawl_web_page(url, crawl_id):
    update_crawl_status(crawl_id, Status.RUNNING)
    try:
        html = crawl_url(url)
        save_webpage(crawl_id, html)
        update_crawl_status(crawl_id, Status.COMPLETE)
    except Exception as e:
        update_crawl_status(crawl_id, Status.ERROR)
