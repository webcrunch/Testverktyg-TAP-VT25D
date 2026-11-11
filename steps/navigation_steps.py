from behave import then
from playwright.sync_api import expect


@then('ska webbläsarfönstrets titel vara "{expected_title}"')
def step_impl(context, expected_title):
    expect(context.page).to_have_title(expected_title)


@then('sidans huvudrubrik (H1) ska vara "{expected_heading}"')
@then('ska sidans huvudrubrik (H1) vara "{expected_heading}"')
def step_impl(context, expected_heading):
    expect(context.reading_list_page.page_h1).to_have_text(expected_heading)


@then('navigeringslänken "{link_name}" ska vara markerad som aktiv')
@then('ska navigeringslänken "{link_name}" vara markerad som aktiv')
def step_impl(context, link_name):
    # Appen markerar den aktiva vyn genom att inaktivera dess knapp
    link_locator = context.reading_list_page.get_nav_link_by_name(link_name)
    expect(link_locator).to_be_disabled()


@then('navigeringslänken "{link_name}" ska inte vara markerad som aktiv')
def step_impl(context, link_name):
    link_locator = context.reading_list_page.get_nav_link_by_name(link_name)
    expect(link_locator).to_be_enabled()
