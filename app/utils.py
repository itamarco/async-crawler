import requests


def crawl_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        return html_content
    else:
        raise Exception(f"Failed to crawl URL. Status code: {response.status_code}")


def save_webpage(crawl_id: str, html_text: str):
    filename = f"{crawl_id}.html"
    with open(f"/tmp/webpages/{filename}", "w", encoding="utf-8") as file:
        file.write(html_text)

