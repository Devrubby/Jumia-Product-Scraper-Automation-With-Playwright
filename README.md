Jumia Product Scraper & Excel Report Automation

Overview
This project is a Python automation tool that scrapes product listings from Jumia Nigeria
using Playwright, performs data cleaning and analysis with pandas, and generates a professionally formatted multi-sheet Excel report using openpyxl.
Unlike static web scraping projects, this scraper interacts with a real-world e-commerce website, handling dynamic content, pagination, and browser automation before transforming the collected data into meaningful business insights.

Features
Searches Jumia for a specified product.
Automates browser interaction with Playwright.
Handles cookie consent automatically.
Scrapes multiple pages of search results.

Extracts:
Product Name
Promo Price
Old Price
Discount
Rating
Number of Reviews
Sponsored Status
Product URL
Cleans and converts scraped data into appropriate data types. Removes duplicate products using the Product URL.
Performs statistical analysis using pandas. Exports a formatted Excel workbook containing multiple reports.

Technologies Used
Python
Playwright
Pandas
openpyxl
Regular Expressions (re)
JSON

Project Structure
Jumia-Product-Scraper-Automation-With-Playwright
Data
  scraped_products.json  #saved here for analysis purpose
Output
  jumia_products_report.xlsx #All scraped details from Jumia
Screenshots:
    Contains sample output pictures of the products scraped excel files.
analysis.py      # Data cleaning and analysis
exporter.py      # Excel report generation
helpers.py       # Helper and extraction functions
main.py          # Application entry point
README.md
scraper.py       # Browser automation and scraping


Excel Report
The generated workbook contains five worksheets:

Products Info: Complete list of scraped products sorted by price.
Summary Statistics: Key metrics such as average price, discounts, ratings, and duplicate count.
Product Insights: Details of notable products, including the most expensive, cheapest, most reviewed, and highest discount items.
Brand Analysis: Product frequency grouped by detected brand.
Price Range Distribution: Distribution of products across predefined price ranges.

Limitations
Brand detection is based on the first word of the product name and may not always represent the actual manufacturer.
Search results depend on Jumia's search algorithm and may include related products in addition to the requested item.
Changes to Jumia's website structure may require updates to the scraper selectors.

Future Improvements
Accept the search term from the command line instead of editing the source code.
Add logging for better monitoring and debugging.
Support exporting charts and visual summaries.
Allow scraping multiple search terms in a single run.

DISCLAIMER
This project is created for educational purposes.
When scraping websites, always respect:
Website terms of service
robots.txt policies where applicable
Reasonable request limits
Data usage regulations
The scraper  only collect publicly available information, not bypass security protections.