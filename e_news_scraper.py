import time

import requests
from bs4 import BeautifulSoup

from scraper import Scraper


class ENewsScraper(Scraper):
    def __init__(self, base_url, html_base, headers):
        super().__init__(base_url, html_base, headers)

    def scrape(self, num_pages):
        for page in range(1, num_pages + 1):
            print(f"Scraping e-news page {page}...")
            soup = self.scrape_page(page, "")
            if not soup:
                continue

            titles, dates = self.extract_details(soup)
            for i in range(len(titles)):
                title = titles[i].get_text(strip=True)
                date = dates[i].get_text(strip=True)
                html_link = titles[i]["href"]
                complete_html_link = f"{self.html_base}{html_link}"

                try:
                    detail_response = requests.get(complete_html_link, headers=self.headers)
                    detail_response.raise_for_status()
                except requests.RequestException as e:
                    print(f"Detail request failed: {e}")
                    continue

                detail_soup = BeautifulSoup(detail_response.text, "html.parser")
                body_div = detail_soup.find("div", class_="content")
                post_content = body_div.find("div", class_="post-content").get_text(separator="", strip=True) \
                    if body_div else "Body content not found"
                html = detail_soup.prettify()

                self.scraped_data.append([date, title, html, post_content])
                time.sleep(1)  # Rate limiting

        self.save_to_csv("scraped_articles.csv")
        print("E-news scraping completed and saved to scraped_articles.csv")
