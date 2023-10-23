import os
import hashlib

import redis
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from tasks import crawl_web_page  # Import the Celery task

app = FastAPI()

redis_url = os.environ.get('REDIS_URL')

redis_client = redis.StrictRedis(redis_url, decode_responses=True)


# Mock storage for crawl data
crawl_data = {}

class CrawlRequest(BaseModel):
    url: str


@app.post("/start_crawl/")
def start_crawl(crawl_request: CrawlRequest):
    # Generate a unique crawl-id
    crawl_id = generate_unique_crawl_id()
    # Acknowledge the request
    crawl_data[crawl_id] = {"status": "Accepted", "url": crawl_request.url}

    crawl_web_page.delay(crawl_request.url, crawl_id)

    return {"crawl_id": crawl_id}


@app.get("/crawl_status/{crawl_id}")
def get_crawl_status(crawl_id: str):
    if crawl_id in crawl_data:
        # Return the status of the crawl
        status = crawl_data[crawl_id]["status"]
        if status == "Complete":
            # If the crawl is complete, return the location of the HTML
            return {"status": status, "html_location": "your_html_location_here"}
        else:
            return {"status": status}
    else:
        raise HTTPException(status_code=404, detail="Crawl-id not found")


def generate_unique_crawl_id(url):
    data = url.encode('utf-8')
    return hashlib.sha1(data).hexdigest()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)