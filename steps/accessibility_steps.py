from behave import when, then
from playwright.sync_api import expect

# Hur många Tab-tryck som får gå åt för att nå ett element innan steget ger upp
MAX_TABS = 25


@when('jag trycker på tangenten "{key}"')
@when('jag trycker på tangenten "{key}" {count:d} gånger')
def step_impl(context, key, count=1):
    """Simulerar tangentbordsnedtryckningar, t.ex. Tab eller Space."""
    for _ in range(count):
        context.page.keyboard.press(key)


@when('jag tabbar till favoritikonen för boken "{title}"')
def step_impl(context, title):
    """Trycker Tab tills hjärtat för boken har fokus, eller misslyckas efter MAX_TABS tryck."""
    star = context.reading_list_page.get_favorite_button(title)
    for _ in range(MAX_TABS):
        context.page.keyboard.press("Tab")
        if star.evaluate("e => e === document.activeElement"):
            return
    raise AssertionError(
        f"Favoritikonen för '{title}' gick inte att nå med Tab ({MAX_TABS} tryck)"
    )


@then('ska navigeringslänken "{link_name}" ha fokus')
def step_impl(context, link_name):
    """Verifierar att den specificerade länken är det nuvarande fokuserade elementet."""
    link_locator = context.reading_list_page.get_nav_link_by_name(link_name)

    # Playwrights metod för att kontrollera fokus
    expect(link_locator).to_be_focused()
