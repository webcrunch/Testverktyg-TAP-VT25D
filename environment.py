# environment.py
from playwright.sync_api import sync_playwright
from pages.reading_list_page import ReadingListPage


def before_all(context):
    """Körs en gång innan alla features. Startar Playwright och webbläsaren."""
    context.playwright_instance = sync_playwright().start()
    # Ändra headless=True till headless=False för GUI-läge (synlig webbläsare)
    context.browser = context.playwright_instance.chromium.launch(headless=True)


def before_scenario(context, scenario):
    """Körs innan varje Scenario. Skapar en ny sida och Page Object."""
    context.page = context.browser.new_page()
    context.reading_list_page = ReadingListPage(context.page)


def after_scenario(context, scenario):
    """Körs efter varje Scenario. Stänger sidan."""
    context.page.close()


def after_all(context):
    """Körs en gång efter alla features. Stänger webbläsare och Playwright."""
    context.browser.close()
    context.playwright_instance.stop()
