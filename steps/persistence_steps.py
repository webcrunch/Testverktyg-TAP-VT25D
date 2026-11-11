from behave import given, when, then
from playwright.sync_api import expect


@given('att jag har lagt till boken "{title}" av "{author}" i katalogen')
def step_impl(context, title, author):
    page = context.reading_list_page
    page.goto_add_book()
    page.title_input.fill(title)
    page.author_input.fill(author)
    page.submit_new_book()

    # Verifiera att boken finns där innan omladdning
    page.goto_catalog()
    expect(page.get_book_locator_by_title(title)).to_be_visible()


@when("jag laddar om sidan")
def step_impl(context):
    context.reading_list_page.reload_page()


@then('ska boken "{title}" inte finnas i katalogen')
def step_impl(context, title):
    book_locator = context.reading_list_page.get_book_locator_by_title(title)
    expect(book_locator).to_have_count(0)
