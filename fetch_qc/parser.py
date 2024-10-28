from bs4 import BeautifulSoup
from .models import Question
import logging


class Parser:
    @staticmethod
    def parse(html_content: str, url: str) -> Question:
        soup = BeautifulSoup(html_content, "html.parser")

        # Extract Question Number
        question_section = soup.find("div", class_="question-discussion-header")
        if not question_section:
            logging.warning(f"Could not find 'question-discussion-header' in {url}")
            return Question(number="UNKNOWN", body="UNKNOWN", choices="UNKNOWN")
        q_num_div = question_section.find("div")
        if q_num_div:
            text = q_num_div.get_text(separator=" ", strip=True)
            if "Question #:" in text:
                question_number = (
                    text.split("Question #:")[1].split("Topic #:")[0].strip()
                )
            else:
                question_number = "UNKNOWN"
        else:
            question_number = "UNKNOWN"

        # Extract Question Body
        question_body_div = soup.find("div", class_="question-body")
        if question_body_div:
            p = question_body_div.find("p", class_="card-text")
            if p:
                question_text = p.get_text(separator=" ", strip=True)
            else:
                question_text = "UNKNOWN"
        else:
            question_text = "UNKNOWN"

        # Extract Question Choices
        choices_div = soup.find("div", class_="question-choices-container")
        if choices_div:
            choices = []
            li_items = choices_div.find_all("li", class_="multi-choice-item")
            for li in li_items:
                span = li.find("span", class_="multi-choice-letter")
                if span:
                    letter = span.get_text(strip=True)
                    span.extract()
                    choice_text = li.get_text(separator=" ", strip=True)
                    choices.append(f"{letter} {choice_text}")
            if not choices:
                choices_text = "VERIFY"
            else:
                choices_text = "\n".join(choices)
        else:
            choices_text = "VERIFY"

        return Question(
            number=question_number, body=question_text, choices=choices_text
        )
