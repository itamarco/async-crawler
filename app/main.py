import os
import hashlib

from fastapi import FastAPI
from pydantic import BaseModel

from status import read_crawl_status
from status import update_crawl_status, Status
from tasks import crawl_web_page  # Import the Celery task

app = FastAPI()

webpages_location = os.environ.get('WEBPAGES_LOCATION')


class CrawlRequest(BaseModel):
    url: str


@app.post("/start_crawl/")
def start_crawl(crawl_request: CrawlRequest):
    crawl_id = generate_unique_crawl_id(crawl_request.url)
    update_crawl_status(crawl_id, Status.ACCEPTED)

    crawl_web_page.delay(crawl_request.url, crawl_id)

    return crawl_id


@app.get("/crawl_status/{crawl_id}")
def get_crawl_status(crawl_id: str):
    status = read_crawl_status(crawl_id) or Status.NOT_FOUND.value

    if status == Status.COMPLETE.value:
        return {"status": status, "html_location": f"{webpages_location}/{crawl_id}.html"}
    else:
        return {"status": status}


def generate_unique_crawl_id(url):
    data = url.encode('utf-8')
    return hashlib.sha1(data).hexdigest()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
