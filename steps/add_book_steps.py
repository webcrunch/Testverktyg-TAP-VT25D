from behave import when, then
from playwright.sync_api import expect

# --- STEG FÖR HANDLING (WHEN) ---


@when('jag fyller i "{text}" i fältet "{field_name}"')
def step_impl(context, text, field_name):
    context.reading_list_page.get_input(field_name).fill(text)


# En tom cell i en Exempel-tabell ger "" i steget, som "{text}" inte matchar
@when('jag fyller i "" i fältet "{field_name}"')
@when('jag lämnar fältet "{field_name}" tomt')
def step_impl(context, field_name):
    context.reading_list_page.get_input(field_name).fill("")


@when('jag klickar på knappen "Lägg till ny bok"')
def step_impl(context):
    context.reading_list_page.submit_new_book()


# --- VERIFIERINGSSTEG (THEN) ---


@then('ska boken "{title}" finnas i katalogen')
def step_impl(context, title):
    book_locator = context.reading_list_page.get_book_locator_by_title(title)
    expect(book_locator).to_be_visible()


@then('boken "{title}" ska inte vara markerad som favorit')
def step_impl(context, title):
    star = context.reading_list_page.get_favorite_button(title)
    expect(star).not_to_have_class("star selected")


@then('ska knappen "Lägg till ny bok" vara inaktiverad')
def step_impl(context):
    expect(context.reading_list_page.add_button).to_be_disabled()


@then('jag ska stanna kvar på sidan "Lägg till bok"')
def step_impl(context):
    # Den aktiva vyns knapp är inaktiverad
    expect(context.reading_list_page.get_nav_link_by_name("Lägg till bok")).to_be_disabled()
    expect(context.reading_list_page.title_input).to_be_visible()


@then('ska fältet "{field_name}" vara tomt')
@then('fältet "{field_name}" ska vara tomt')
def step_impl(context, field_name):
    current_value = context.reading_list_page.get_input_value(field_name)
    assert (
        current_value == ""
    ), f"Fel: Fältet '{field_name}' skulle vara tomt, men innehåller: '{current_value}'"
