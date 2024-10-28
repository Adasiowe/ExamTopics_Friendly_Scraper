
# ExamTopics Scraper - Functional, but work in progress

This project consists of two Python scripts designed to scrape exam questions and choices from [ExamTopics](https://www.examtopics.com):

1. `fetch_urls.py`: Fetches a list of discussion URLs for a selected provider and saves them to a file in the `urls` folder.
2. `fetch_q&c.py`: Scrapes the questions, choices, and suggested answers from the fetched URLs.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Step 1: Fetch URLs](#step-1-fetch-urls)
  - [Step 2: Fetch Questions and Choices](#step-2-fetch-questions-and-choices)
- [Output Files](#output-files)
- [Notes](#notes)
- [Disclaimer](#disclaimer)

## Prerequisites

- **Python 3.x**: Ensure you have Python installed. You can download it from [here](https://www.python.org/downloads/).
- **Required Python Packages**: Listed in `requirements.txt`.

## Installation

1. **Clone the Repository or Download the Scripts**

   Clone the repository:

   ```bash
   git clone https://github.com/Adasiowe/ExamTopics_Simple_Scraper.git
Or download the scripts directly from the repository.
    
2.  **Install the Required Packages**
    
    `pip install -r requirements.txt` 
    

## Usage

### Step 1: Fetch URLs

Run the `fetch_urls.py` script to fetch discussion URLs for a selected provider.

`python fetch_urls.py` 

**Process:**

-   **Provider Selection**: When prompted, enter the number corresponding to the provider you wish to scrape.
-   **Scraping**: The script will scrape all pages for the selected provider.
-   **Output**: URLs will be saved to a text file named `{provider}_urls.txt` in the `urls` folder (e.g., `urls/microsoft_urls.txt`).

### Step 2: Fetch Questions and Choices

1.  **Prepare URL Files**
    
    -   Ensure that all URL files are located in the `urls` folder. This folder is created automatically by `fetch_urls.py`.
2.  **Run the Scraper**
    
    `python fetch_q&c.py` 
    

**Process:**

-   **Reading URLs**: The script reads all `.txt` files in the `urls` folder.
-   **Fetching Data**: For each URL, it fetches the question, choices, and suggested answer.
-   **Output**: The scraped data is saved to `exam_questions.csv`.

## Output Files

-   **`urls/{provider}_urls.txt`**: Contains the list of discussion URLs for the selected provider, saved in the `urls` folder.
-   **`exam_questions.csv`**: Contains the scraped questions, choices, and suggested answers.

## Notes

-   **Delays Between Requests**: The scripts include random delays between requests to avoid overwhelming the server.
-   **Failed URLs**: If any URLs fail to fetch, they will be listed at the end of the script's output.
-   **Custom Headers**: The scripts use custom headers to mimic real browser requests. It didn't work for me otherwise.