from behave import given, when, then
from playwright.sync_api import expect


@when('jag trycker på tangenten "{key}"')
@when('jag trycker på tangenten "{key}" {count:d} gånger')
def step_impl(context, key, count=1):
    """Simulerar tangentbordsnedtryckningar, t.ex. Tab eller Space."""
    for _ in range(count):
        context.page.keyboard.press(key)


@then('Så ska navigeringslänken "{link_name}" ha fokus')
def step_impl(context, link_name):
    """Verifierar att den specificerade länken är det nuvarande fokuserade elementet."""
    # Hämta lokatorn för länken
    link_locator = context.reading_list_page.get_nav_link_by_name(link_name)

    # Playwrights metod för att kontrollera fokus
    expect(link_locator).to_be_focused()
