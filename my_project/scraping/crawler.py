import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import time
import random
from config.settings import USER_AGENT, RAW_DATA_PATH, MAX_DEPTH

class WebCrawler:
    def __init__(self):
        self.visited_urls = set()

    def fetch_page(self, url):
        """Fetches a web page and returns its content."""
        headers = {"User-Agent": USER_AGENT}
        try:
            response = requests.get(url, headers=headers, timeout=5)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Failed to fetch {url}: {e}")
            return None

    def extract_links(self, url, html):
        """Extracts all hyperlinks from a given webpage."""
        soup = BeautifulSoup(html, "html.parser")
        links = set()
        for anchor in soup.find_all("a", href=True):
            full_url = urljoin(url, anchor["href"])
            if full_url.startswith("http"):
                links.add(full_url)
        return links

    def crawl(self, url, depth=0):
        """Recursively crawls websites up to a certain depth."""
        if depth > MAX_DEPTH or url in self.visited_urls:
            return

        print(f"Crawling: {url}")
        self.visited_urls.add(url)

        html = self.fetch_page(url)
        if html:
            self.save_raw_data(url, html)
            links = self.extract_links(url, html)
            time.sleep(random.uniform(1, 3))  # Avoid rate limiting

            for link in links:
                self.crawl(link, depth + 1)

    def save_raw_data(self, url, html):
        """Saves raw HTML content to a file."""
        os.makedirs(RAW_DATA_PATH, exist_ok=True)
        filename = os.path.join(RAW_DATA_PATH, f"{hash(url)}.html")
        with open(filename, "w", encoding="utf-8") as file:
            file.write(html)
        print(f"Saved: {filename}")

# Run the crawler
if __name__ == "__main__":
    crawler = WebCrawler()
    start_url = "https://example.com"
    crawler.crawl(start_url)
