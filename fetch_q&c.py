import requests
from bs4 import BeautifulSoup
import csv
import time
import random
import os
import glob

class QuestionScraper:
    def __init__(self, url_folder='urls'):
        self.url_folder = url_folder
        self.urls = self.load_urls()
        self.failed_urls = []

    def load_urls(self):
        urls = []
        for file_path in glob.glob(os.path.join(self.url_folder, '*.txt')):
            with open(file_path, 'r', encoding='utf-8') as file:
                urls.extend([line.strip() for line in file if line.strip()])
        return urls

    def fetch_and_parse(self, url, retries=3):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }
        for attempt in range(retries):
            try:
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    question_section = soup.find('div', class_='question-discussion-header')
                    question_body = soup.find('div', class_='question-body')
                    choices_section = soup.find('div', class_='question-choices-container')
                    suggested_answer = soup.find('span', class_='correct-answer')

                    if not question_section or not question_body or not choices_section or not suggested_answer:
                        print(f"Could not parse question data from {url}")
                        return None

                    question_text = question_body.find('p', class_='card-text').text.strip()
                    choices = choices_section.find_all('li', class_='multi-choice-item')
                    choices_text = []
                    for choice in choices:
                        letter = choice.find('span', class_='multi-choice-letter').text.strip()
                        choice_text = letter + ' ' + choice.text.replace(letter, '').strip()
                        choices_text.append(choice_text)
                    suggested_answer_text = suggested_answer.text.strip()
                    return {
                        'url': url,
                        'question': question_text,
                        'choices': choices_text,
                        'suggested_answer': suggested_answer_text
                    }
                elif response.status_code == 503:
                    print(f"Failed to fetch {url} with status code 503. Retrying... (Attempt {attempt + 1}/{retries})")
                    time.sleep(random.uniform(5, 10))
                else:
                    print(f"Failed to fetch {url} with status code {response.status_code}")
                    return None
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                time.sleep(random.uniform(3, 7))
        print(f"Failed to fetch {url} after {retries} attempts")
        return None

    def scrape_questions(self):
        print(f"Attempting to fetch {len(self.urls)} questions.")
        with open('exam_questions.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['URL', 'Question', 'Choices', 'Suggested Answer'])
            for idx, url in enumerate(self.urls, start=1):
                data = self.fetch_and_parse(url)
                if data:
                    choices_text = '\n'.join(data['choices'])
                    writer.writerow([data['url'], data['question'], choices_text, data['suggested_answer']])
                    print(f"Question #{idx} fetched successfully.")
                else:
                    self.failed_urls.append(url)
                delay = random.uniform(1, 3)
                print(f"Waiting for {delay:.2f} seconds before next request...")
                time.sleep(delay)
        print("\nData saved to exam_questions.csv")
        if not self.failed_urls:
            print("All questions were fetched successfully.")
        else:
            print("Some questions failed to be fetched:")
            for url in self.failed_urls:
                print(url)

def main():
    scraper = QuestionScraper()
    scraper.scrape_questions()

if __name__ == "__main__":
    main()
