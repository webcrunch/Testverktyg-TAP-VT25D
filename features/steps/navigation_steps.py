from behave import then
from playwright.sync_api import expect


@then('ska webbläsarfönstrets titel vara "{expected_title}"')
def step_impl(context, expected_title):
    expect(context.page).to_have_title(expected_title)


@then('Och sidans huvudrubrik (H1) ska vara "{expected_heading}"')
def step_impl(context, expected_heading):
    expect(context.reading_list_page.page_h1).to_have_text(expected_heading)


@then('Och navigeringslänken "{link_name}" ska vara markerad som aktiv')
def step_impl(context, link_name):
    link_locator = context.reading_list_page.get_nav_link_by_name(link_name)

    # Kontrollerar antingen ARIA-attribut eller CSS-klass för aktiv status
    try:
        expect(link_locator).to_have_attribute("aria-current", "page", timeout=500)
    except AssertionError:
        expect(link_locator).to_have_class("*active*", timeout=500)
