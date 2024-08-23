import requests
from bs4 import BeautifulSoup
import csv
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Scraper:
    def __init__(self, base_url, html_base, headers):
        self.base_url = base_url
        self.html_base = html_base
        self.headers = headers
        self.scraped_data = []

    def scrape_page(self, page_number, url_suffix):
        url = f"{self.base_url}{url_suffix}{page_number}"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return

        soup = BeautifulSoup(response.text, "html.parser")
        return soup

    @staticmethod
    def extract_details(soup):
        titles = soup.find_all("a", class_="ContentGrid")
        dates = soup.find_all("td", class_="col-xs-1 recordListDate")
        return titles, dates

    def save_to_csv(self, filename):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["date", "title", "html", "body"])
            writer.writerows(self.scraped_data)
