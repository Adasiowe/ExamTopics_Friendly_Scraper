
# ExamTopics Friendly Scraper

This project consists of two main scripts: `fetch_urls.py` for collecting discussion URLs for a chosen provider, and `fetch_qc.py` for scraping question content and saving it as CSV files. The project is organized into modular packages for handling requests, parsing HTML, and managing data storage.

## Prerequisites

1.  **Install Required Packages**: Install the necessary Python packages using `requirements.txt`. Run the following command in the project root directory:
    
    `pip install -r requirements.txt`

## Folder Structure

-   **`fetch_qc/`**: Contains modules for scraping question content and storing it in CSV format.
-   **`fetch_urls/`**: Contains modules for scraping discussion URLs for different providers.
-   **`urls/`**: Stores the URL lists for each provider in `{provider}_urls.txt` files.
-   **`scraped_discussions/`**: Stores the CSV files with scraped question data, named by provider and exam (if applicable).
-   **`fetch_qc.py`**: Main script for scraping questions.
-   **`fetch_urls.py`**: Main script for fetching URLs.

----------

### Step 1: Fetch URLs

Run the `fetch_urls.py` script to fetch discussion URLs for a selected provider:

`python fetch_urls.py` 

**Process:**

-   **Provider Selection**: When prompted, enter the number corresponding to the provider you wish to scrape.
-   **Scraping**: The script will scrape all pages for the selected provider.
-   **Output**: URLs will be saved to a text file named `{provider}_urls.txt` in the `urls` folder (e.g., `urls/microsoft_urls.txt`).

----------

### Step 2: Fetch Questions and Choices

1.  **Prepare URL Files**
    
    -   Ensure that all URL files are located in the `urls` folder. This folder is created automatically by `fetch_urls.py`. Each file should follow the format `{provider}_urls.txt`.
2.  **Run the Question Scraper**
    
    `python fetch_qc.py` 
    

**Process:**

-   **Provider and Exam Selection**:
    -   The script prompts the user to select a provider from a list.
    -   For certain providers (only Google and HashiCorp at the moment), the user is further prompted to choose a specific exam or certification (e.g., Google’s "Professional Cloud Architect" or HashiCorp’s "Vault Associate").
-   **Reading URLs**:
    -   The script reads the `.txt` file for the chosen provider from the `urls` folder.
    -   If an exam or certification is selected, the script filters URLs to match the chosen exam or certification.
-   **Fetching Data**:
    -   For each URL, the script fetches the question, choices, and suggested answer.
-   **Output**:
    -   The scraped data is saved to a dynamically named CSV file in the `scraped_discussions` folder.

----------

## Output Files

-   **`urls/{provider}_urls.txt`**:
    -   Contains the list of discussion URLs for the selected provider, saved in the `urls` folder.
-   **`scraped_discussions/{provider}-{exam_name}.csv`**:
    -   Contains the scraped questions, choices, and suggested answers for the specified provider and exam/certification, saved in the `scraped_discussions` folder.
    -   If no exam or certification is selected, the file is named `{provider}.csv`.

----------

## Notes

-   **Non-Commercial Use Only**: This script is intended for personal, non-commercial use. The data it retrieves is freely available on the public internet, and this tool simply automates the retrieval process for convenience. Use responsibly pls.
-   **Data Accessibility**: All data collected by this tool is publicly accessible on the internet; this tool does not bypass any protections. It is designed to collect data that you could access manually by browsing.
-   **Delays Between Requests**: The scripts include random delays between requests to avoid overwhelming the server.
-   **Predownloaded Files**: Several urls.txt files and scraped discussions can be found in this repo. They are current as of 29.10.2024. 