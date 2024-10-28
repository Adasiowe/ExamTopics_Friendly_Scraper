# # data_storage.py
# import csv
# import os
# from models import Question

# class DataStorage:
#     @staticmethod
#     def save_questions(questions, csv_path):
#         # Ensure the output directory exists
#         output_dir = os.path.dirname(csv_path)
#         os.makedirs(output_dir, exist_ok=True)

#         with open(csv_path, mode="w", newline="", encoding="utf-8") as file:
#             writer = csv.DictWriter(
#                 file,
#                 fieldnames=["Question Number", "Question Body", "Question Choices"],
#             )
#             writer.writeheader()
#             for question in questions:
#                 writer.writerow({
#                     "Question Number": question.number,
#                     "Question Body": question.body,
#                     "Question Choices": question.choices
#                 })

# fetch_qc/data_storage.py
import csv
import os
import logging
from typing import List
from fetch_qc.models import Question

class DataStorage:
    @staticmethod
    def save_questions(questions: List[Question], output_dir: str = "scraped_discussions", provider: str = "") -> None:
        """
        Saves the list of questions to a CSV file within the specified output directory.

        Args:
            questions (List[Question]): List of Question objects to save.
            output_dir (str, optional): Directory to save the CSV file. Defaults to "scraped_discussions".
            provider (str, optional): Name of the provider to name the file. Defaults to "".
        """
        os.makedirs(output_dir, exist_ok=True)

        if provider:
            csv_filename = f"{provider.lower()}.csv"
        else:
            csv_filename = "scraped_questions.csv"

        csv_path = os.path.join(output_dir, csv_filename)

        try:
            with open(csv_path, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=["Question Number", "Question Body", "Question Choices"],
                )
                writer.writeheader()
                for question in questions:
                    writer.writerow({
                        "Question Number": question.number,
                        "Question Body": question.body,
                        "Question Choices": question.choices
                    })
            logging.info(f"Data saved to '{csv_path}'.")
        except IOError as e:
            logging.error(f"Error writing to file '{csv_path}': {e}")

