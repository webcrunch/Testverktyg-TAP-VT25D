from behave import given, when, then
from playwright.sync_api import expect

# --- GENERISKA STEG (GIVEN) ---


@given('att jag är på sidan "{page_title}"')
def step_impl(context, page_title):
    context.reading_list_page.goto_home()
    expect(context.page).to_have_title(page_title)


@given('att boken "{title}" är markerad som favorit')
def step_impl(context, title):
    context.reading_list_page.goto_home()
    context.reading_list_page.click_favorite_button(title)


# --- STEG FÖR HANDLING (WHEN) ---


@when('jag klickar på favoritikonen för boken "{title}"')
@when('jag klickar på favoritikonen för boken "{title}" {click_count:d} gånger')
def step_impl(context, title, click_count=1):
    for _ in range(click_count):
        context.reading_list_page.click_favorite_button(title)


@when('jag navigerar till sidan "Mina böcker"')
def step_impl(context):
    context.reading_list_page.goto_my_books()


# --- VERIFIERINGSSTEG (THEN) ---


@then('ska boken "{title}" visas i listan')
def step_impl(context, title):
    book_locator = context.reading_list_page.get_book_locator_by_title(title)
    expect(book_locator).to_be_visible()


@then('ska boken "{title}" inte visas i listan')
def step_impl(context, title):
    book_locator = context.reading_list_page.get_book_locator_by_title(title)
    expect(book_locator).not_to_be_visible()


@then('ska boken "{title}" visas i listan om "{should_exist}" är "Ja"')
def step_impl(context, title, should_exist):
    book_locator = context.reading_list_page.get_book_locator_by_title(title)

    if should_exist.lower() == "ja":
        expect(book_locator).to_be_visible()
    else:
        expect(book_locator).not_to_be_visible()


@then("och antalet favoriter ska vara {expected_count:d}")
def step_impl(context, expected_count):
    current_count = context.reading_list_page.get_favorite_count()
    assert (
        current_count == expected_count
    ), f"Fel: Förväntade {expected_count} favoriter, men hittade {current_count}."
