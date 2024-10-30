import logging
import os
from fetch_urls.provider_scraper import ProviderScraper


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    providers = {
        1: "Microsoft",
        2: "Cisco",
        3: "CompTia",
        4: "Amazon",
        5: "Oracle",
        6: "Isaca",
        7: "VMware",
        8: "Salesforce",
        9: "PMI",
        10: "Google",
        11: "PRINCE2",
        12: "Databricks",
        13: "HashiCorp",
        14: "CrowdStrike",
        15: "Linux-Foundation",
        16: "Python-Institute",
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

    # Check if the URL file already exists
    provider_file = f"{provider.lower()}_urls.txt"
    file_path = os.path.join("urls", provider_file)

    if os.path.exists(file_path):
        print(f"\nThe file '{provider_file}' already exists in the 'urls' folder.")
        while True:
            user_input = input(
                "Do you want to overwrite it or skip the scraping? (Enter 'overwrite' or 'skip'): "
            ).strip().lower()
            if user_input == 'overwrite':
                # Proceed with scraping and overwriting the file
                break
            elif user_input == 'skip':
                print("Skipping the scraping. Exiting.")
                return  # Exit the script
            else:
                print("Invalid input. Please enter 'overwrite' or 'skip'.")

    scraper = ProviderScraper(provider)
    last_page = scraper.fetch_total_pages()
    print(f"\n{last_page} pages will be scraped for provider '{provider}'.\n")
    scraper.scrape_pages(last_page)
    scraper.save_urls()


if __name__ == "__main__":
    main()
