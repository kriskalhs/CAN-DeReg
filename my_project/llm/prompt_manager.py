import openai
import os
from config.settings import OPENAI_API_KEY, PROCESSED_DATA_PATH

class PromptManager:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY

    def summarize_text(self, text):
        """Uses OpenAI's API to summarize a given text."""
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "Summarize this text"},
                      {"role": "user", "content": text}],
            temperature=0.5
        )
        return response["choices"][0]["message"]["content"]

    def summarize_all(self):
        """Reads all processed text files and summarizes them."""
        summaries = {}
        for filename in os.listdir(PROCESSED_DATA_PATH):
            file_path = os.path.join(PROCESSED_DATA_PATH, filename)

            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()

            summary = self.summarize_text(text)
            summaries[filename] = summary
            print(f"Summary for {filename}:\n{summary}\n")

        return summaries

# Run the summarizer
if __name__ == "__main__":
    pm = PromptManager()
    pm.summarize_all()
