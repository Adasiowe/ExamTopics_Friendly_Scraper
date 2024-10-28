# http_client.py
import requests
import time
import random
import logging
from typing import Optional


class HTTPClient:
    def __init__(self, headers=None, timeout=10):
        self.headers = headers or {"User-Agent": "Mozilla/5.0"}
        self.timeout = timeout

    def get(self, url: str, retries: int = 3) -> Optional[requests.Response]:
        for attempt in range(1, retries + 1):
            try:
                response = requests.get(url, headers=self.headers, timeout=self.timeout)
                if response.status_code == 200:
                    return response
                else:
                    logging.warning(
                        f"Failed to fetch {url} with status code {response.status_code}. "
                        f"Retrying... (Attempt {attempt}/{retries})"
                    )
            except requests.exceptions.RequestException as e:
                logging.error(
                    f"An error occurred while fetching {url}: {e}. "
                    f"Retrying... (Attempt {attempt}/{retries})"
                )
            time.sleep(random.uniform(1, 3))
        logging.error(f"Failed to fetch {url} after {retries} attempts.")
        return None
