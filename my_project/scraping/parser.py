from bs4 import BeautifulSoup
import os
from config.settings import RAW_DATA_PATH, PROCESSED_DATA_PATH

class HTMLParser:
    def __init__(self):
        os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)

    def extract_text(self, html):
        """Extracts readable text from an HTML page."""
        soup = BeautifulSoup(html, "html.parser")
        for script in soup(["script", "style"]):  # Remove scripts and styles
            script.decompose()
        return soup.get_text(separator="\n", strip=True)

    def process_raw_files(self):
        """Parses all raw HTML files and extracts text."""
        for filename in os.listdir(RAW_DATA_PATH):
            raw_path = os.path.join(RAW_DATA_PATH, filename)
            processed_path = os.path.join(PROCESSED_DATA_PATH, filename.replace(".html", ".txt"))

            with open(raw_path, "r", encoding="utf-8") as file:
                html = file.read()
            
            text = self.extract_text(html)
            with open(processed_path, "w", encoding="utf-8") as file:
                file.write(text)
            print(f"Processed: {processed_path}")

# Run the parser
if __name__ == "__main__":
    parser = HTMLParser()
    parser.process_raw_files()
