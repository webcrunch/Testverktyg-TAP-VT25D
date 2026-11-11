from behave import given, when, then, step
from playwright.sync_api import expect

# --- GENERISKA STEG (GIVEN) ---


@given('att jag är på sidan "{page_title}"')
def step_impl(context, page_title):
    context.reading_list_page.goto_home()
    expect(context.page).to_have_title(page_title)


@given('att boken "{title}" är markerad som favorit')
def step_impl(context, title):
    context.reading_list_page.goto_catalog()
    context.reading_list_page.click_favorite_button(title)
    expect(context.reading_list_page.get_favorite_button(title)).to_have_class("star selected")


# --- STEG FÖR HANDLING (WHEN) ---


@when('jag klickar på favoritikonen för boken "{title}"')
@when('jag klickar på favoritikonen för boken "{title}" {click_count:d} gånger')
def step_impl(context, title, click_count=1):
    for _ in range(click_count):
        context.reading_list_page.click_favorite_button(title)


# step: används både som När och som Och efter ett Så
@step('jag navigerar till sidan "{name}"')
def step_impl(context, name):
    context.reading_list_page.goto(name)


# --- VERIFIERINGSSTEG (THEN) ---


@then('ska boken "{title}" visas i listan')
@then('boken "{title}" visas i listan')
def step_impl(context, title):
    expect(context.reading_list_page.get_favorite_locator_by_title(title)).to_be_visible()


@then('ska boken "{title}" inte visas i listan')
def step_impl(context, title):
    expect(context.reading_list_page.get_favorite_locator_by_title(title)).to_have_count(0)


@then('ska boken "{title}" visas i listan om "{should_exist}" är "Ja"')
def step_impl(context, title, should_exist):
    favorite = context.reading_list_page.get_favorite_locator_by_title(title)

    if should_exist.lower() == "ja":
        expect(favorite).to_be_visible()
    else:
        expect(favorite).to_have_count(0)


@then("antalet favoriter ska vara {expected_count:d}")
@then("ska antalet favoriter vara {expected_count:d}")
def step_impl(context, expected_count):
    current_count = context.reading_list_page.get_favorite_count()
    assert (
        current_count == expected_count
    ), f"Fel: Förväntade {expected_count} favoriter, men hittade {current_count}."
