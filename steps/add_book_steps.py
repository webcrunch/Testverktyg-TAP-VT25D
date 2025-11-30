from behave import when, then
from playwright.sync_api import expect

# --- STEG FÖR HANDLING (WHEN) ---


@when('jag navigerar till sidan "Lägg till bok"')
def step_impl(context):
    context.reading_list_page.goto_add_book()


@when('jag navigerar till sidan "Läslistan"')
def step_impl(context):
    context.reading_list_page.goto_home()


@when('jag fyller i "{text}" i fältet "{field_name}"')
def step_impl(context, text, field_name):
    if "Titel" in field_name:
        context.reading_list_page.title_input.fill(text)
    elif "Författare" in field_name:
        context.reading_list_page.author_input.fill(text)
    else:
        raise ValueError(f"Okänt fält: {field_name}")


@when('jag lämnar fältet "{field_name}" tomt')
def step_impl(context, field_name):
    if "Titel" in field_name:
        context.reading_list_page.title_input.fill("")
    elif "Författare" in field_name:
        context.reading_list_page.author_input.fill("")


@when('jag klickar på knappen "Lägg till"')
def step_impl(context):
    context.reading_list_page.submit_new_book()


# --- VERIFIERINGSSTEG (THEN) ---


@then('så ska boken "{title}" finnas i katalogen')
def step_impl(context, title):
    book_locator = context.reading_list_page.get_book_locator_by_title(title)
    expect(book_locator).to_be_visible()


@then('Och boken "{title}" ska inte vara markerad som favorit')
def step_impl(context, title):
    context.reading_list_page.goto_my_books()
    book_locator = context.reading_list_page.get_book_locator_by_title(title)
    expect(book_locator).not_to_be_visible()
    context.reading_list_page.goto_home()


@then('Så ska ett felmeddelande visas för fältet "Titel"')
def step_impl(context):
    error_message_locator = context.reading_list_page.get_validation_error_message()
    expect(error_message_locator).to_be_visible()
    expect(error_message_locator).to_have_text("Fältet är obligatoriskt")


@then('Och jag ska stanna kvar på sidan "Lägg till bok"')
def step_impl(context):
    expect(context.reading_list_page.add_button).to_be_visible()


@then('Så ska fältet "{field_name}" vara tomt')
@then('Och fältet "{field_name}" ska vara tomt')
def step_impl(context, field_name):
    current_value = context.reading_list_page.get_input_value(field_name)
    assert (
        current_value == ""
    ), f"Fel: Fältet '{field_name}' skulle vara tomt, men innehåller: '{current_value}'"
