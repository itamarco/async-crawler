# async-crawler

A Python-based web crawler that can be used to extract and store HTML content from web pages.

![Architecture](https://github.com/itamarco/async-crawler/raw/master/async-crawler.png)

### Prerequisites

- docker-compose

For dev:
- Python
- Poetry

### Installation

1. Clone the repository.
2. Install required dependencies using `poetry install`.


### Usage
```
docker-compose up -d
```
It listens on host's port 8000 
```
[POST]
/start_crawl
{
    url: "https://www.exmaple.com"
}


[GET]
/crawl_status/<crawl_id>
```

### Python dependencies
- fastapi
- uvicorn
- celery
- redis
- requests