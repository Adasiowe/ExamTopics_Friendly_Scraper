import os
import requests
from bs4 import BeautifulSoup

class ProviderScraper:
    def __init__(self, provider_name):
        self.provider_name = provider_name.lower()
        self.base_url = f'https://www.examtopics.com/discussions/{self.provider_name}/'
        self.all_urls = []

    def fetch_total_pages(self):
        response = requests.get(self.base_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            pagination_info = soup.find('span', class_='discussion-list-page-indicator')
            if pagination_info:
                strong_tags = pagination_info.find_all('strong')
                if len(strong_tags) >= 2:
                    try:
                        last_page = int(strong_tags[1].text.strip())
                        return last_page
                    except ValueError:
                        print("Error parsing page numbers. Defaulting to 1 page.")
            else:
                print("Could not find pagination info. Defaulting to 1 page.")
        else:
            print(f"Failed to retrieve the first page. Status code: {response.status_code}")
        return 1

    def scrape_pages(self, last_page):
        for page_number in range(1, last_page + 1):
            page_url = f"{self.base_url}{page_number}/"
            print(f"Scraping page {page_number}: {page_url}")
            response = requests.get(page_url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                divs = soup.find_all('div', class_='discussion-title-container')
                for div in divs:
                    a_tag = div.find('a', class_='discussion-link')
                    if a_tag and 'href' in a_tag.attrs:
                        href = a_tag['href']
                        full_url = 'https://www.examtopics.com' + href
                        self.all_urls.append(full_url)
            else:
                print(f"Failed to retrieve page {page_number}. Status code: {response.status_code}")

    def save_urls(self):
        # Ensure the 'urls' directory exists
        output_dir = 'urls'
        os.makedirs(output_dir, exist_ok=True)

        # Define the output file path within the 'urls' directory
        output_file = os.path.join(output_dir, f"{self.provider_name}_urls.txt")
        
        with open(output_file, 'w') as f:
            for url in self.all_urls:
                f.write(url + '\n')
        print(f"\nScraped {len(self.all_urls)} URLs. Saved to '{output_file}'.")

def main():
    providers = {
        1: 'Microsoft',
        2: 'Cisco',
        3: 'CompTia',
        4: 'Amazon',
        5: 'Oracle',
        6: 'Isaca',
        7: 'VMware',
        8: 'Salesforce',
        9: 'PMI',
        10: 'Google',
        11: 'PRINCE2',
        12: 'Databricks',
        13: 'HashiCorp'
    }
    
    print("Choose a provider by entering the corresponding number:")
    for num, name in providers.items():
        print(f"{num}. {name}")
    
    while True:
        try:
            choice = int(input("Enter provider number: ").strip())
            if choice in providers:
                provider = providers[choice]
                break
            else:
                print("Invalid choice. Please select a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    scraper = ProviderScraper(provider)
    last_page = scraper.fetch_total_pages()
    print(f"\n{last_page} pages will be scraped for provider '{provider}'.\n")
    scraper.scrape_pages(last_page)
    scraper.save_urls()

if __name__ == "__main__":
    main()
