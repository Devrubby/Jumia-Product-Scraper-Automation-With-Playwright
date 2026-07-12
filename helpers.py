import json, re
from playwright.sync_api import TimeoutError
from pathlib import Path
BASE_URL = "https://jumia.com.ng"

def save_json_data(data, file_name="scraped_products.json"):
    input_path  = Path("Data")
    input_path.mkdir(exist_ok=True)
    saved_file_path = input_path / file_name
    with open(saved_file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)



def safe_extract(parent_locator, child_selector, timeout=500):
    try:
        element = parent_locator.locator(child_selector)
        if element.is_visible(timeout=timeout):
            return element.text_content().strip()
    except TimeoutError:
        return None

def accept_cookie(arg):
    try:
        button = arg.locator(".btn._sec._md.-fw.-plm")
        button.click(timeout=200)
        button.wait_for(state="hidden", timeout=3000)
        print("Cookie button clicked")
    except TimeoutError:
        print("Accept cookie button not found")
#
def product_search(locator_obj, search_term):
    try:
        search_bar = locator_obj.get_by_role("textbox", name="Search")
        search_bar.press_sequentially(search_term, delay=200)
        search_bar.press("Enter")
        search_button = locator_obj.locator(".btn._prim._md._search.-fsh0.-rad24")
        search_button.click()
        return search_term
    except TypeError as e:
        print(f"Error: {e}")
        return None


def extract_price(text):
    if not text:
        return None
    match = re.search(r"[\d,]+(?:\.\d+)?", text)
    if match:
        return  float(match.group().replace(",", ""))
    return  None

def extract_reviews_count(text):
    if not text:
        return  None
    match = re.search(r"\((\d+)\)", text)
    return int(match.group(1)) if match else 0

def extract_ratings(text):
    if not text:
        return  None
    match = re.search(r"\d+(\.\d+)?", text)
    return  float(match.group()) if match else None

def extract_products(page_obj):
    products_list = []
    products_locator = page_obj.locator("article.prd, div[data-spon='true'], section.prd")
    products_locator.first.wait_for(state="attached", timeout=12000)
    product_elements = products_locator.all()
    print(f"\n Total products  captured on the page: {len(product_elements)}")
    # Extract product attributes
    for element in product_elements:
        is_sponsored = element.get_attribute("data-spon") == "true" or "sponsored" in (
                element.get_attribute("class") or "").lower()
        prod_name = safe_extract(element, ".name")
        price = extract_price(safe_extract(element, ".prc"))
        old_price = extract_price(safe_extract(element, ".old"))
        discount = safe_extract(element, ".bdg._dsct")
        rating = extract_ratings(safe_extract(element, ".stars"))
        num_reviews = extract_reviews_count(safe_extract(element, ".rev"))
        prod_url = f"{BASE_URL}{element.locator(".core").get_attribute("href")}"
        products_list.append({"Product Name": prod_name, "Promo Price": price,
            "Old Price": old_price, "Discount": discount, "Rating": rating,
            "Sponsored": is_sponsored, "Number of Reviews": num_reviews, "Product URL": prod_url
        })
    return products_list