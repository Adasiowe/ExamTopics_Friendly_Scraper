# fetch_qc.py
import os
import logging
from fetch_qc.question_scraper import QuestionScraper

def main():
    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

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

    google_exams = {
        1: "professional-machine-learning-engineer",
        2: "google-analytics",
        3: "video-advertising",
        4: "individual-qualification",
        5: "search-advertising",
        6: "professional-cloud-developer",
        7: "professional-cloud-network-engineer",
        8: "professional-data-engineer",
        9: "adwords-fundamentals",
        10: "associate-cloud-engineer",
        11: "professional-cloud-security-engineer",
        12: "professional-google-workspace-administrator",
        13: "professional-cloud-devops-engineer",
        14: "professional-cloud-architect",
        15: "professional-cloud-database-engineer",
        16: "professional-collaboration-engineer",
        17: "professional-chromeos-administrator",
        18: "gsuite",
        19: "cloud-digital-leader",
    }

    hashicorp_exams = {1: "vault-associate", 2: "terraform-associate"}

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

    # Initialize variables
    exam_string = None
    hashicorp_filter = None

    # If provider is Google, prompt for exam selection
    if choice == 10:
        print("\nChoose an exam by entering the corresponding number:")
        for num, name in google_exams.items():
            display_name = name.replace("-", " ").title()
            print(f"{num}. {display_name}")
        while True:
            try:
                exam_choice = int(input("Enter exam number: ").strip())
                if exam_choice in google_exams:
                    exam_string = google_exams[exam_choice]
                    break
                else:
                    print("Invalid choice. Please select a number from the list.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    # If provider is HashiCorp, prompt for filter selection
    elif choice == 13:
        print("\nChoose a certification by entering the corresponding number:")
        for num, name in hashicorp_exams.items():
            display_name = name.replace("-", " ").title()
            print(f"{num}. {display_name}")
        while True:
            try:
                filter_choice = int(input("Enter certification number: ").strip())
                if filter_choice in hashicorp_exams:
                    hashicorp_filter = hashicorp_exams[filter_choice]
                    break
                else:
                    print("Invalid choice. Please select a number from the list.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    # Construct the file name based on provider
    provider_file = f"{provider.lower()}_urls.txt"
    file_path = os.path.join("urls", provider_file)

    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"\nThe file '{provider_file}' does not exist in the 'urls' folder.")
        print("Please run the URL fetching script 'fetch_urls.py' first to generate the required URL file.")
        return

    # Load URLs based on provider and exam/filter (if Google or HashiCorp for now)
    if choice == 10:
        with open(file_path, "r", encoding="utf-8") as f:
            all_urls = [line.strip() for line in f if line.strip()]

        filtered_urls = [url for url in all_urls if exam_string in url.lower()]
        if not filtered_urls:
            print(
                f"\nNo URLs found for the selected exam '{exam_string.replace('-', ' ').title()}'."
            )
            return
        print(
            f"\nFound {len(filtered_urls)} URLs for the selected exam '{exam_string.replace('-', ' ').title()}'."
        )
        urls_to_scrape = filtered_urls
    elif choice == 13:
        with open(file_path, "r", encoding="utf-8") as f:
            all_urls = [line.strip() for line in f if line.strip()]

        filtered_urls = [url for url in all_urls if hashicorp_filter in url.lower()]
        if not filtered_urls:
            print(
                f"\nNo URLs found for the selected certification '{hashicorp_filter.replace('-', ' ').title()}'."
            )
            return
        print(
            f"\nFound {len(filtered_urls)} URLs for the selected certification '{hashicorp_filter.replace('-', ' ').title()}'."
        )
        urls_to_scrape = filtered_urls
    else:
        # For other providers, load all URLs
        with open(file_path, "r", encoding="utf-8") as f:
            urls_to_scrape = [line.strip() for line in f if line.strip()]
        if not urls_to_scrape:
            print(f"\nNo URLs found in the file '{provider_file}'.")
            return
        print(f"\nFound {len(urls_to_scrape)} URLs for provider '{provider}'.")

    # Initialize the scraper and scrape the questions
    scraper = QuestionScraper(urls_to_scrape)
    scraper.scrape_questions(provider, exam_string or hashicorp_filter)

if __name__ == "__main__":
    main()
