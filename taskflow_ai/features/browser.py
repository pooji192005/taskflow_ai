from playwright.sync_api import sync_playwright

def search(query):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(f"https://www.google.com/search?q={query}")