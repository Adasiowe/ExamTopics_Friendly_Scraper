# # provider_scraper.py
# import time
# import random
# import logging
# from http_client import HTTPClient
# from parser import Parser
# from data_storage import DataStorage
# from typing import List


# class ProviderScraper:
#     def __init__(self, provider_name: str):
#         self.provider_name = provider_name.lower()
#         self.base_url = f"https://www.examtopics.com/discussions/{self.provider_name}/"
#         self.all_urls: List[str] = []
#         self.http_client = HTTPClient()

#     def fetch_total_pages(self) -> int:
#         logging.info(f"Fetching the first page to determine total pages: {self.base_url}")
#         response = self.http_client.get(self.base_url)
#         if response:
#             last_page = Parser.parse_total_pages(response.text)
#             logging.info(
#                 f"Detected {last_page} pages for provider '{self.provider_name.capitalize()}'."
#             )
#             return last_page
#         else:
#             logging.error("Failed to fetch the first page. Defaulting to 1 page.")
#             return 1

#     def scrape_pages(self, last_page: int) -> None:
#         for page_number in range(1, last_page + 1):
#             page_url = f"{self.base_url}{page_number}/"
#             logging.info(f"Scraping page {page_number}: {page_url}")
#             response = self.http_client.get(page_url)
#             if response:
#                 page_urls = Parser.parse_page_urls(response.text)
#                 self.all_urls.extend(page_urls)
#             else:
#                 logging.error(f"Failed to retrieve page {page_number}.")
#             # Respectful scraping: wait between 0.5 to 1.5 seconds
#             delay = random.uniform(0.5, 1.5)
#             logging.info(f"Waiting for {delay:.2f} seconds before next request...")
#             time.sleep(delay)

#     def save_urls(self) -> None:
#         DataStorage.save_urls(self.all_urls, self.provider_name)

# fetch_urls/provider_scraper.py
import time
import random
import logging
from .http_client import HTTPClient
from .parser import Parser
from .data_storage import DataStorage
from typing import List

class ProviderScraper:
    def __init__(self, provider_name: str):
        self.provider_name = provider_name.lower()
        self.base_url = f"https://www.examtopics.com/discussions/{self.provider_name}/"
        self.all_urls: List[str] = []
        self.http_client = HTTPClient()

    def fetch_total_pages(self) -> int:
        logging.info(f"Fetching the first page to determine total pages: {self.base_url}")
        response = self.http_client.get(self.base_url)
        if response:
            last_page = Parser.parse_total_pages(response.text)
            logging.info(
                f"Detected {last_page} pages for provider '{self.provider_name.capitalize()}'."
            )
            return last_page
        else:
            logging.error("Failed to fetch the first page. Defaulting to 1 page.")
            return 1

    def scrape_pages(self, last_page: int) -> None:
        for page_number in range(1, last_page + 1):
            page_url = f"{self.base_url}{page_number}/"
            logging.info(f"Scraping page {page_number}: {page_url}")
            response = self.http_client.get(page_url)
            if response:
                page_urls = Parser.parse_page_urls(response.text)
                self.all_urls.extend(page_urls)
            else:
                logging.error(f"Failed to retrieve page {page_number}.")
            # Respectful scraping: wait between 0.5 to 1.5 seconds
            delay = random.uniform(0.5, 1.5)
            logging.info(f"Waiting for {delay:.2f} seconds before next request...")
            time.sleep(delay)

    def save_urls(self) -> None:
        DataStorage.save_urls(self.all_urls, self.provider_name)

