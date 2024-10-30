import time
import random
import logging
import os
from .http_client import HTTPClient
from .parser import Parser
from .data_storage import DataStorage
from .models import Question
from typing import List, Optional


class QuestionScraper:
    def __init__(self, urls: List[str]):
        self.urls = urls
        self.failed_urls: List[str] = []
        self.http_client = HTTPClient()

    def fetch_and_parse(self, url: str, retries: int = 3) -> Optional[Question]:
        response = self.http_client.get(url, retries=retries)
        if response:
            question = Parser.parse(response.text, url)
            if question.number == "UNKNOWN" and question.body == "UNKNOWN":
                logging.warning(f"Failed to parse question from {url}")
                self.failed_urls.append(url)
                return None
            return question
        else:
            self.failed_urls.append(url)
            return None

    def scrape_questions(self, provider: str, exam_name: Optional[str], csv_path: str) -> None:
        # Define the output directory
        output_dir = "../scraped_discussions"
        os.makedirs(output_dir, exist_ok=True)  # Create the folder if it doesn't exist
        if exam_name:
            csv_filename = f"{provider.lower()}-{exam_name.lower()}.csv"
        else:
            csv_filename = f"{provider.lower()}.csv"
        csv_path = os.path.join(output_dir, csv_filename)
        logging.info(f"\nAttempting to fetch {len(self.urls)} questions.\n")
        questions = []

        for idx, url in enumerate(self.urls, start=1):
            logging.info(f"Fetching Question #{idx} from URL: {url}")
            question = self.fetch_and_parse(url)
            if question:
                questions.append(question)
                logging.info(f"Question #{idx} fetched successfully.\n")
            else:
                logging.warning(f"Question #{idx} failed to fetch.\n")
            # Respectful scraping: wait between 1 to 2 seconds
            delay = random.uniform(1, 2)
            logging.info(f"Waiting for {delay:.2f} seconds before next request...\n")
            time.sleep(delay)

        # Save the questions
        DataStorage.save_questions(questions, csv_path)

        if not self.failed_urls:
            logging.info("All questions were fetched successfully.")
        else:
            logging.info("\nSome questions failed to be fetched:")
            for url in self.failed_urls:
                logging.info(url)
