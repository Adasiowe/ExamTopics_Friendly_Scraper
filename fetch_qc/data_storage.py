import csv
import os
import logging
from typing import List
from .models import Question


class DataStorage:
    @staticmethod
    def save_questions(questions: List[Question], provider: str = "") -> None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(base_dir, "..", "scraped_discussions")
        os.makedirs(output_dir, exist_ok=True)

        # Create the CSV filename based on the provider name
        csv_filename = f"{provider.lower()}" if provider else "scraped_questions.csv"
        csv_path = os.path.join(output_dir, csv_filename)

        try:
            with open(csv_path, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=["Question Number", "Question Body", "Question Choices"],
                )
                writer.writeheader()
                for question in questions:
                    writer.writerow(
                        {
                            "Question Number": question.number,
                            "Question Body": question.body,
                            "Question Choices": question.choices,
                        }
                    )
            logging.info(f"Data saved to '{csv_path}'.")
        except IOError as e:
            logging.error(f"Error writing to file '{csv_path}': {e}")
