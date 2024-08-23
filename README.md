# Web Scraping Script

This Python script scrapes various types of articles (press releases, e-news, in-the-news, and editorials) from a set of web pages and saves the data into a CSV file. The script uses `requests` to fetch the HTML content and `BeautifulSoup` to parse the HTML and extract relevant data. It also utilizes `dotenv` for managing environment variables.

## Prerequisites

- Python 3.x
- `requests`
- `beautifulsoup4`
- `python-dotenv`
- `pprint` (optional, for pretty printing)

You can install the required libraries using `pip`:

```bash
pip install requests beautifulsoup4 python-dotenv
```

## Setup

1. **Create a `.env` File**

   Create a file named `.env` in the root of your project directory. Add the following environment variables to the `.env` file with the appropriate URLs:

   ```env
   HTML_BASE=https://example.com/base
   PRESS_RELEASES_URL=https://example.com/press-releases?page=
   E_NEWS_URL=https://example.com/e-news?page=
   IN_THE_NEWS_URL=https://example.com/in-the-news?page=
   EDITORIAL_URL=https://example.com/editorials?page=
   ```

2. **Script Configuration**

   Ensure that the environment variables in your `.env` file match the URLs you wish to scrape.

## Running the Script

To run the script, simply execute it using Python:

```bash
python your_script_name.py
```

The script will:

- Scrape press releases from pages 1 to 155.
- Scrape e-news articles from pages 1 to 5.
- Scrape in-the-news articles from pages 1 to 50.
- Scrape editorials from pages 1 to 7.

Data from all these sources will be saved into a CSV file named `scraped_articles.csv` in the same directory as the script.

## Notes

- The script includes delays (using `time.sleep(1)`) between requests to avoid overloading the server.
- If the server responds with a status code other than 200, the script will print an error message and continue to the next page.

## Example Output

The `scraped_articles.csv` file will contain the following columns:
- `date`: The date of the article.
- `title`: The title of the article.
- `html`: The HTML content of the article.
- `body`: The text body of the article.

## Troubleshooting

- If you encounter issues with authentication or access, ensure that the URLs are correct and that you have the necessary permissions.
- Check that your `.env` file is correctly formatted and that all required environment variables are set.

## License

This script is provided as-is. Feel free to modify and use it according to your needs.
