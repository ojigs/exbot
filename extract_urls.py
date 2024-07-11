"""
This script extracts URLs from specified websites and saves them to text files.
It fetches the content of each website, parses the HTML to find all anchor tags,
and writes the URLs to a file named after the website.
"""

from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup


def extract_urls(base_url, timeout=10):
    """Extract URLs from a given base URL."""
    try:
        response = requests.get(base_url, timeout=timeout)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to retrieve {base_url}: {e}")
        return []
    soup = BeautifulSoup(response.content, "html.parser")
    urls = []

    for link in soup.find_all("a", href=True):
        url = urljoin(base_url, link["href"])
        urls.append(url)
    return urls


def save_urls_to_file(urls, filename):
    """Save extracted URLs to a file."""
    with open(filename, "w", encoding="utf-8") as file:
        for url in urls:
            file.write(url + "\n")


def main():
    """Main function to extract and save URLs from specified websites."""
    websites = [
        'https://jd-claude.com.ng'
    ]

    for website in websites:
        urls = extract_urls(website)
        if urls:
            filename = f'{website.replace("https://", "").replace("http://", "").replace("/", "_")}_urls.txt'
            save_urls_to_file(urls, filename)
            print(f"URLs from {website} have been saved to {filename}")


if __name__ == "__main__":
    main()
