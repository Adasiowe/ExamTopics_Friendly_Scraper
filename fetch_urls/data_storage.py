# # data_storage.py
# import os
# import logging
# from typing import List


# class DataStorage:
#     @staticmethod
#     def save_urls(urls: List[str], provider_name: str, output_dir: str = "urls") -> None:
#         os.makedirs(output_dir, exist_ok=True)
#         output_file = os.path.join(output_dir, f"{provider_name}_urls.txt")

#         try:
#             with open(output_file, "w", encoding="utf-8") as f:
#                 for url in urls:
#                     f.write(url + "\n")
#             logging.info(f"Scraped {len(urls)} URLs. Saved to '{output_file}'.")
#         except IOError as e:
#             logging.error(f"Error writing to file '{output_file}': {e}")

# fetch_urls/data_storage.py
import os
import logging
from typing import List

class DataStorage:
    @staticmethod
    def save_urls(urls: List[str], provider_name: str, output_dir: str = "urls") -> None:
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, f"{provider_name.lower()}_urls.txt")

        try:
            with open(output_file, "w", encoding="utf-8") as f:
                for url in urls:
                    f.write(url + "\n")
            logging.info(f"Scraped {len(urls)} URLs. Saved to '{output_file}'.")
        except IOError as e:
            logging.error(f"Error writing to file '{output_file}': {e}")

