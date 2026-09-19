# Book-Scraper-Selenium
# Books to Scrape - Selenium Web Scraper

A robust web automation and scraping tool built with **Python** and **Selenium** to extract book details across multiple pages from [Books to Scrape](https://books.toscrape.com/) and save them into a structured CSV file.

## Features
- **Dynamic Pagination:** Automatically traverses through all pages using a resilient `while` loop and exception handling until no pages are left.
- **Data Extraction:** Pulls book titles, prices, and cover image links.
- **CSV Export:** Automatically saves the scraped data with proper UTF-8 encoding.

## Technologies Used
- Python 3.x
- Selenium WebDriver
- CSV Module

## How to Run
1. Make sure you have Selenium installed:
   ```bash
   pip install selenium
