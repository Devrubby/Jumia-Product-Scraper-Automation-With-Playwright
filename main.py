import pandas as pd
from openpyxl.workbook import Workbook
from playwright.sync_api import sync_playwright
from pathlib import  Path

from scraper import  run
from helpers import save_json_data
from analysis import get_unique_product, summary_stats, brand_analysis, find_price_range
from exporter import(create_products_sheet, create_summary_sheet,create_insight_sheet,
create_brand_sheet, create_price_range_sheet)

SEARCH_TERM = "Laptops" #The product to search for on Jumia
OUTPUT_PATH = Path("Output")



with (sync_playwright() as playwright):
    scraped_data = run(playwright, SEARCH_TERM)
    save_json_data(scraped_data)
    products_df = pd.DataFrame(scraped_data["Products"]).sort_values(
        by="Promo Price", ascending=False
    )
    unique_df = get_unique_product(products_df)
    summary = summary_stats(unique_df, products_df)
    brands = brand_analysis(unique_df)
    ranges = find_price_range(unique_df)
    wkb = Workbook()
    create_products_sheet(wkb, products_df)
    create_summary_sheet(wkb, summary, SEARCH_TERM)
    create_insight_sheet(wkb, summary)
    create_brand_sheet(wkb, brands)
    create_price_range_sheet(wkb, ranges)
    wkb.save(OUTPUT_PATH/"jumia_products_report.xlsx")