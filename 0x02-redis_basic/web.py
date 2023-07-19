#!/usr/bin/env python3
"""
Web Cache and Tracker
"""
import redis
import requests
from typing import Dict

# Create Redis connection
redis_client = redis.Redis()


def get_page(url: str) -> str:
    # Check if URL is already cached
    cached_html = redis_client.get(url)
    if cached_html:
        # URL is cached, increment access count
        count_key = f"count:{url}"
        redis_client.incr(count_key)
        return cached_html.decode()

    # URL is not cached, retrieve HTML content
    response = requests.get(url)
    html_content = response.text

    # Cache HTML content with 10-second expiration
    redis_client.setex(url, 10, html_content)

    # Increment access count
    count_key = f"count:{url}"
    redis_client.incr(count_key)

    return html_content


def get_access_count(url: str) -> int:
    # Retrieve access count for the URL
    count_key = f"count:{url}"
    access_count = redis_client.get(count_key)
    if access_count:
        return int(access_count)
    return 0


if __name__ == '__main__':
    url = "http://slowwly.robertomurray.co.uk/delay/1000/url/" \
          "https://example.com"
    page_content = get_page(url)
    print(page_content)

    access_count = get_access_count(url)
    print(f"Access count for {url}: {access_count}")
