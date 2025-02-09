from scraping.crawler import WebCrawler
from scraping.parser import HTMLParser
from llm.prompt_manager import PromptManager

def main():
    start_url = "https://example.com"

    print("Starting the crawler...")
    crawler = WebCrawler()
    crawler.crawl(start_url)

    print("Parsing HTML files...")
    parser = HTMLParser()
    parser.process_raw_files()

    print("Generating summaries...")
    pm = PromptManager()
    pm.summarize_all()

if __name__ == "__main__":
    main()
