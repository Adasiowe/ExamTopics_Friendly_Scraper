from bs4 import BeautifulSoup
from typing import List
import logging


class Parser:
    @staticmethod
    def parse_total_pages(html_content: str) -> int:
        soup = BeautifulSoup(html_content, "html.parser")
        pagination_info = soup.find("span", class_="discussion-list-page-indicator")
        if pagination_info:
            strong_tags = pagination_info.find_all("strong")
            if len(strong_tags) >= 2:
                try:
                    last_page = int(strong_tags[1].text.strip())
                    return last_page
                except ValueError:
                    logging.error("Error parsing page numbers. Defaulting to 1 page.")
            else:
                logging.error(
                    "Pagination info not found properly. Defaulting to 1 page."
                )
        else:
            logging.error("Could not find pagination info. Defaulting to 1 page.")
        return 1

    @staticmethod
    def parse_page_urls(html_content: str) -> List[str]:
        soup = BeautifulSoup(html_content, "html.parser")
        # Include both correct and typo class names
        divs = soup.find_all(
            "div",
            class_=["discussion-title-container", "dicussion-title-container"],
        )
        logging.info(f"Found {len(divs)} discussion containers on the page.")

        urls = []
        for div in divs:
            a_tag = div.find("a", class_="discussion-link")
            if a_tag and "href" in a_tag.attrs:
                href = a_tag["href"]
                full_url = "https://www.examtopics.com" + href
                urls.append(full_url)
            else:
                logging.warning(
                    "Warning: 'a' tag with class 'discussion-link' not found in a div."
                )
        return urls
