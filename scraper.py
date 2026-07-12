from playwright.sync_api import sync_playwright, TimeoutError
from helpers import(
    extract_products, accept_cookie, product_search
)


BASE_URL = "https://jumia.com.ng"


def run(playwright, search_term):
    all_products = []
    with playwright.chromium.launch(headless=False) as browser:
        context = browser.new_context()
        page = context.new_page()
        page.goto(BASE_URL)
        accept_cookie(page)
        searched_term = product_search(page, search_term)
        page.wait_for_selector(".-phm.-gy5", timeout=10000)
        page.wait_for_load_state("domcontentloaded")
        while True:
            print(f"\n Currently scraping {page.url}")
            #Scrolling because I suspect the website is using lazy loading to load Dom content
            for i in range(3):
                page.evaluate("window.scrollBy(0, 800)")
                page.wait_for_timeout(350)
            page.evaluate("window.scrollTo(0, 0)")
            products = extract_products(page)
            all_products.extend(products)
            try:
                next_page = page.get_by_role("link", name="Next Page")
                if not next_page.is_visible():
                    print("Currently at the end of the page")
                    break
                else:
                    next_page.click()
            except TimeoutError as e:
                print(f"Error: {e}")
        return  {
            "Searched Term": searched_term,
            "Products": all_products
        }