import os
from press_releases_scraper import PressReleasesScraper
from e_news_scraper import ENewsScraper
from in_the_news_scraper import InTheNewsScraper
from editorials_scraper import EditorialsScraper


def main():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Upgrade-Insecure-Requests": "1"
    }

    base_url = os.getenv("PRESS_RELEASES_URL")
    html_base = os.getenv("HTML_BASE")

    press_releases_scraper = PressReleasesScraper(base_url, html_base, headers)
    press_releases_scraper.scrape(num_pages=155)

    base_url = os.getenv("E_NEWS_URL")
    e_news_scraper = ENewsScraper(base_url, html_base, headers)
    e_news_scraper.scrape(num_pages=6)

    base_url = os.getenv("IN_THE_NEWS_URL")
    in_the_news_scraper = InTheNewsScraper(base_url, html_base, headers)
    in_the_news_scraper.scrape(num_pages=51)

    base_url = os.getenv("EDITORIAL_URL")
    editorials_scraper = EditorialsScraper(base_url, html_base, headers)
    editorials_scraper.scrape(num_pages=7)


if __name__ == "__main__":
    main()
