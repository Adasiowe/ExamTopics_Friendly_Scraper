import logging
from fetch_qc.question_scraper import QuestionScraper
import os


def setup_logging():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def display_options(options_dict, title):
    print(f"\n{title}")
    for num, name in options_dict.items():
        print(f"{num}. {name}")


def get_user_choice(options_dict, prompt):
    while True:
        try:
            choice = int(input(f"{prompt}: ").strip())
            if choice in options_dict:
                return options_dict[choice]
            else:
                print("Invalid choice. Please select a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def filter_urls(all_urls, filter_string):
    return [url for url in all_urls if filter_string.lower() in url.lower()]


def main():
    setup_logging()

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

    microsoft_exams = {
        1: "ai-100",
        2: "ai-102",
        3: "ai-900",
        4: "az-100",
        5: "az-101",
        6: "az-102",
        7: "az-103",
        8: "az-104",
        9: "az-120",
        10: "az-140",
        11: "az-200",
        12: "az-202",
        13: "az-203",
        14: "az-204",
        15: "az-220",
        16: "az-300",
        17: "az-301",
        18: "az-302",
        19: "az-303",
        20: "az-304",
        21: "az-305",
        22: "az-400",
        23: "az-500",
        24: "az-600",
        25: "az-700",
        26: "az-720",
        27: "az-800",
        28: "az-801",
        29: "az-900",
        30: "da-100",
        31: "dp-100",
        32: "dp-200",
        33: "dp-201",
        34: "dp-203",
        35: "dp-300",
        36: "dp-420",
        37: "dp-500",
        38: "dp-600",
        39: "dp-900",
        40: "mb-200",
        41: "mb-210",
        42: "mb-220",
        43: "mb-230",
        44: "mb-240",
        45: "mb-260",
        46: "mb-300",
        47: "mb-310",
        48: "mb-320",
        49: "mb-330",
        50: "mb-335",
        51: "mb-340",
        52: "mb-400",
        53: "mb-500",
        54: "mb-600",
        55: "mb-700",
        56: "mb-800",
        57: "mb-820",
        58: "mb-900",
        59: "mb-901",
        60: "mb-910",
        61: "mb-920",
        62: "mb2-715",
        63: "mb2-716",
        64: "mb2-717",
        65: "mb2-718",
        66: "mb2-719",
        67: "mb6-894",
        68: "mb6-896",
        69: "mb6-897",
        70: "mb6-898",
        71: "md-100",
        72: "md-101",
        73: "md-102",
        74: "mo-201",
        75: "ms-100",
        76: "ms-101",
        77: "ms-102",
        78: "ms-200",
        79: "ms-201",
        80: "ms-202",
        81: "ms-203",
        82: "ms-220",
        83: "ms-300",
        84: "ms-301",
        85: "ms-302",
        86: "ms-500",
        87: "ms-600",
        88: "ms-700",
        89: "ms-720",
        90: "ms-721",
        91: "ms-740",
        92: "ms-900",
        93: "pl-100",
        94: "pl-200",
        95: "pl-300",
        96: "pl-400",
        97: "pl-500",
        98: "pl-600",
        99: "pl-900",
        100: "sc-100",
        101: "sc-200",
        102: "sc-300",
        103: "sc-400",
        104: "sc-900",
    }

    providers_with_exams = {
        "Google": google_exams,
        "HashiCorp": hashicorp_exams,
        "Microsoft": microsoft_exams,
    }

    print("Choose a provider by entering the corresponding number:")
    display_options(providers, "Providers:")

    provider_choice = get_user_choice(providers, "Enter provider number")
    provider = provider_choice

    # Initialize variables
    selected_exam = None
    urls_to_scrape = []

    # Check if the selected provider has certifications
    if provider in providers_with_exams:
        exams = providers_with_exams[provider]
        exam_title = f"Choose a {'Microsoft' if provider == 'Microsoft' else provider} exam by entering the corresponding number:"
        display_options(exams, exam_title)
        selected_exam = get_user_choice(exams, "Enter exam number")

    # Construct the file name based on provider
    provider_file = f"{provider.lower()}_urls.txt"
    file_path = os.path.join("urls", provider_file)

    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"\nThe file '{provider_file}' does not exist in the 'urls' folder.")
        print(
            "Please run the URL fetching script 'fetch_urls.py' first to generate the required URL file."
        )
        return

    # Load URLs based on provider and exam (if applicable)
    with open(file_path, "r", encoding="utf-8") as f:
        all_urls = [line.strip() for line in f if line.strip()]

    if selected_exam:
        filtered_urls = filter_urls(all_urls, selected_exam)
        if not filtered_urls:
            print(f"\nNo URLs found for the selected exam '{selected_exam.upper()}'.")
            return
        print(
            f"\nFound {len(filtered_urls)} URLs for the selected exam '{selected_exam.upper()}'."
        )
        urls_to_scrape = filtered_urls
    else:
        # For providers without exams, use all URLs
        urls_to_scrape = all_urls
        if not urls_to_scrape:
            print(f"\nNo URLs found in the file '{provider_file}'.")
            return
        print(f"\nFound {len(urls_to_scrape)} URLs for provider '{provider}'.")

    # Initialize the scraper
    scraper = QuestionScraper(urls_to_scrape)
    scraper.scrape_questions(provider, selected_exam)


if __name__ == "__main__":
    main()
