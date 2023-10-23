import requests

def crawl_url(url):
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text

        return html_content
    else:
        raise Exception(f"Failed to crawl URL. Status code: {response.status_code}")


