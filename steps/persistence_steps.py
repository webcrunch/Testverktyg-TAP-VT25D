from behave import given, when, then
from playwright.sync_api import expect


@given('att jag har lagt till boken "{title}" av "{author}" i katalogen')
def step_impl(context, title, author):
    # Använder logik från add_book_steps.py
    context.reading_list_page.goto_add_book()
    context.reading_list_page.title_input.fill(title)
    context.reading_list_page.author_input.fill(author)
    context.reading_list_page.submit_new_book()

    # Verifiera att boken finns där innan omladdning
    context.reading_list_page.goto_home()
    book_locator = context.reading_list_page.get_book_locator_by_title(title)
    expect(book_locator).to_be_visible()


@when("jag laddar om sidan")
def step_impl(context):
    context.reading_list_page.reload_page()


@then('Så ska boken "{title}" inte finnas i katalogen')
def step_impl(context, title):
    book_locator = context.reading_list_page.get_book_locator_by_title(title)
    expect(book_locator).not_to_be_visible()
