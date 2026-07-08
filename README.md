This project demonstrates a web scraping automation workflow using Python and Playwright
to extract product information from Jumia, a dynamic e-commerce website.
Unlike traditional static HTML scraping approaches, this project uses browser automation to interact with a live website
where content is dynamically loaded through JavaScript.
The scraper automates a real browser session, navigates through product search pages, extracts structured product information, 
handles pagination, cleans the collected data, and exports the final dataset into an organized Excel report.
This project was built to simulate a practical automation task that could be requested by a business needing product monitoring,
market research, competitor analysis, or price tracking.

Objectives
The goal of this project is to build a reusable E-commerce scraping automation tool capable of:
Automating browser interactions using Playwright
Scraping dynamically rendered web content
Extracting product details from search result pages
Handling multiple pages of results
Cleaning and structuring scraped data
Removing duplicate records
Exporting results into a professional Excel report
Generating summary statistics from collected data

Programming Language Used
Python

Libraries and Tools

Playwright
Used for browser automation and interacting with dynamically generated web pages.
Features used:
Launching browser sessions
Navigating web pages
Waiting for dynamic elements
Locating page elements
Extracting rendered content
Handling pagination


Pandas
Used for:
Data cleaning
Data transformation
Duplicate removal
Data analysis
Generating summary statistics

OpenPyXL
Used for:
Creating Excel workbooks
Formatting spreadsheets
Adjusting column widths
Applying styles to reports

Pathlib
Used for:
Managing project directories
Handling input and output file paths

Project Structure
Jumia-Product-Scraper/
main.py
scraper/
browser.py
scraper.py
analysis/
analysis.py
reports/
excel_report.py│
data/
scraped_products.json
output/
jumia_products_report.xlsx
requirements.txt
README.md

How It Works
1. Browser Automation
The scraper launches a Chromium browser using Playwright.
Instead of sending direct HTTP requests, the program behaves like a real user:
Opens Jumia
Searches for products
Waits for JavaScript generated content
Reads the rendered page
This approach allows the scraper to work with modern websites where product information is not available in the initial HTML response.

2. Product Search
The scraper accepts a search query and navigates to the corresponding Jumia search results page.
Example:
Laptop
The scraper collects products matching the search term.
3. Data Extraction
For each product, the scraper extracts information such as:
Product name, product price, product rating, number of reviews, product URL , seller information (if available)
product availability, search category

4. Example output:
Product name         Price          Rating      Reviews     URL     
HP Laptop 15     ₦350,000      4.5           120       product_url

   
5. Pagination Handling
The scraper automatically moves through multiple result pages.
The workflow:
Scrape current page
Extract product information
Check for next page
Navigate to next page
Repeat until target page limit is reached
6. Data Cleaning
Before exporting the final report, the collected data is processed.
Cleaning operations include:
Removing duplicate products
Cleaning price formatting
Converting prices into numeric values
Handling missing values
Standardizing column names
7. Data Analysis
The project generates useful insights from the scraped products.
Examples:
Total products collected
Average product price
Highest priced product
Lowest priced product
Average rating
Number of products by category
8. Excel Report Generation
The final output is exported into a formatted Excel workbook.
The workbook contains multiple sheets:
Products Sheet
Contains all scraped product information.

Example columns:
Product Name, price, rating, reviews, seller, product URL

Summary Sheet
Contains overall statistics:
Example:
Total Products: 250,   Average Price: ₦120,500,   Highest Price: ₦850,000 , Average Rating: 4.2

Category Analysis Sheet
Contains grouped analysis such as:
Products per category, Average price per category, Rating distribution,

Installation
Clone Repository
git clone repository_url
Navigate into the project:
cd Jumia-Product-Scraper
Create Virtual Environment
python -m venv .venv
Activate environment:
Windows:
.venv\Scripts\activate
Linux/Mac:
source .venv/bin/activate
Install Dependencies
pip install -r requirements.txt
Install Playwright browsers:
playwright install

Running The Project
Run:
python main.py
The scraper will:
Launch the browser
Search Jumia products
Extract product information
Clean the data
Generate an Excel report
The final report will be saved inside:
output/

Example Use Cases
This automation can be adapted for:
Price Monitoring
Track product price changes over time.
Example:
Electronics prices
Laptop prices
Smartphone prices
Market Research
Collect product information to analyze:
Competitor pricing
Product popularity
Market trends
Inventory Research
Businesses can collect information about:
Available products
Sellers
Product categories


Challenges Encountered
Dynamic Websites
Modern websites load content through JavaScript, meaning traditional scraping methods may not capture the required information.

Solution:
Used Playwright browser automation to interact with the rendered page.
Changing Website Structure
E-commerce websites frequently change their HTML structure.

Solution:
Created reusable selectors and separated scraping logic from reporting logic.

Data Cleaning
Raw scraped data often contains:
Currency symbols
Missing values
Duplicate products

Solution:
Used pandas to clean and transform collected data.

Future Improvements
Possible improvements include:
Add scheduled scraping
Store historical price data
Create price comparison dashboards
Add database storage
Implement automatic email reports
Add support for multiple e-commerce websites
Deploy scraper as a web service

DISCLAIMER
This project is created for educational purposes.
When scraping websites, always respect:
Website terms of service
robots.txt policies where applicable
Reasonable request limits
Data usage regulations
The scraper  only collect publicly available information, not bypass security protections.