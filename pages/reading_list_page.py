from playwright.sync_api import Page, Locator


class ReadingListPage:

    BASE_URL = "https://tap-vt25-testverktyg.github.io/exam--reading-list/"

    # Navigeringsknapparnas namn -> data-testid. "Läslistan" (appens namn) är katalogvyn.
    NAV_TEST_IDS = {
        "Katalog": "catalog",
        "Läslistan": "catalog",
        "Lägg till bok": "add-book",
        "Mina böcker": "favorites",
    }

    def __init__(self, page: Page):
        self.page = page

        # --- Navigering och globala selektorer ---
        self.page_h1: Locator = page.locator("h1")
        self.catalog: Locator = page.locator(".catalog")
        # Listan på Mina böcker
        self.favorite_list: Locator = page.get_by_test_id("book-list")

        # --- Lägg till bok-selektorer ---
        self.title_input: Locator = page.get_by_test_id("add-input-title")
        self.author_input: Locator = page.get_by_test_id("add-input-author")
        self.add_button: Locator = page.get_by_test_id("add-submit")

    # --- Navigering och Övergripande Metoder ---

    def goto_home(self):
        self.page.goto(self.BASE_URL)

    def get_nav_link_by_name(self, name: str) -> Locator:
        if name not in self.NAV_TEST_IDS:
            raise ValueError(f"Okänd navigeringsknapp: {name}")
        return self.page.get_by_test_id(self.NAV_TEST_IDS[name])

    def goto(self, name: str):
        # Den aktiva vyns knapp är inaktiverad, så den klickas bara när vyn inte redan är vald
        link = self.get_nav_link_by_name(name)
        if link.is_enabled():
            link.click()

    def goto_catalog(self):
        self.goto("Katalog")

    def goto_my_books(self):
        self.goto("Mina böcker")

    def goto_add_book(self):
        self.goto("Lägg till bok")

    def reload_page(self):
        self.page.reload()

    # --- Favorit och Bok Metoder ---

    def get_book_locator_by_title(self, title: str) -> Locator:
        """En bok i katalogen."""
        return self.catalog.locator(".book").filter(
            has=self.page.get_by_test_id(f"star-{title}")
        )

    def get_favorite_button(self, title: str) -> Locator:
        return self.page.get_by_test_id(f"star-{title}")

    def click_favorite_button(self, title: str):
        self.get_favorite_button(title).click()

    def get_favorite_locator_by_title(self, title: str) -> Locator:
        """En bok i listan på Mina böcker."""
        return self.page.get_by_test_id(f"fav-{title}")

    def get_favorite_count(self) -> int:
        """Raderna på Mina böcker, eller de markerade hjärtana när katalogen visas."""
        # En tom lista har ingen höjd och räknas inte som synlig, så vyn avgörs av den aktiva knappen
        if self.get_nav_link_by_name("Mina böcker").is_disabled():
            return self.favorite_list.locator("li").count()
        self.catalog.wait_for(state="visible")
        return self.catalog.locator(".star.selected").count()

    # --- Lägg till bok/Formulär Metoder ---

    def submit_new_book(self):
        self.add_button.click()

    def get_input(self, field_name: str) -> Locator:
        if field_name == "Titel":
            return self.title_input
        if field_name == "Författare":
            return self.author_input
        raise ValueError(f"Okänt fält: {field_name}")

    def get_input_value(self, field_name: str) -> str:
        return self.get_input(field_name).input_value()
