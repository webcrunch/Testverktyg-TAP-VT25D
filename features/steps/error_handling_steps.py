from behave import given, when, then
from playwright.sync_api import expect


@given("att servern är nere och ger felkod 500 vid försök att lägga till bok")
def step_impl(context):
    """Sätter upp Playwrights router för att simulera ett 500-fel."""
    context.reading_list_page.simulate_add_book_failure()


@then("Så ska ett felmeddelande visas för nätverksfelet")
def step_impl(context):
    """Verifierar att felnotisen är synlig och innehåller en feltext."""
    error_locator = context.reading_list_page.get_error_notification()
    expect(error_locator).to_be_visible()
    # Antar att appen visar en feltext som inkluderar "fel" eller "kunde inte"
    expect(error_locator).to_have_text("Kunde inte spara")


@then('Och boken "{title}" ska inte finnas i katalogen')
def step_impl(context, title):
    """Verifierar att boken inte lades till."""
    context.reading_list_page.goto_home()
    book_locator = context.reading_list_page.get_book_locator_by_title(title)
    expect(book_locator).not_to_be_visible()
