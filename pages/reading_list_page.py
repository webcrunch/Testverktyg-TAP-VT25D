from playwright.sync_api import Page, Locator


class ReadingListPage:

    BASE_URL = "https://tap-vt25-testverktyg.github.io/exam--reading-list/"

    def __init__(self, page: Page):
        self.page = page

        # --- Navigering och Globala Selektorer ---
        self.home_link: Locator = page.get_by_test_id("nav-link-home")
        self.my_books_link: Locator = page.get_by_test_id("nav-link-favorites")
        self.add_book_link: Locator = page.get_by_test_id("nav-link-add")
        self.favorite_count_badge: Locator = page.get_by_test_id("favorite-count-badge")
        self.book_list: Locator = page.get_by_test_id("book-list")
        self.page_h1: Locator = page.locator("h1")

        # --- Lägg till bok-selektorer ---
        self.title_input: Locator = page.get_by_test_id("input-title")
        self.author_input: Locator = page.get_by_test_id("input-author")
        self.add_button: Locator = page.get_by_test_id("submit-add-book")
        self.validation_message: Locator = page.locator(
            "[data-testid='input-title'] + .invalid-feedback"
        )

        # --- Felhantering Selektor (Antagen) ---
        self.error_notification: Locator = page.locator(".alert.alert-danger")

    # --- Navigering och Övergripande Metoder ---

    def goto_home(self):
        self.page.goto(self.BASE_URL)

    def goto_my_books(self):
        self.my_books_link.click()

    def goto_add_book(self):
        self.add_book_link.click()

    def reload_page(self):
        self.page.reload()

    # --- Favorit och Bok Metoder ---

    def get_book_locator_by_title(self, title: str) -> Locator:
        return (
            self.book_list.locator("[data-testid='book-card']")
            .filter(has_text=title)
            .first
        )

    def get_favorite_button(self, title: str) -> Locator:
        book_locator = self.get_book_locator_by_title(title)
        return book_locator.get_by_test_id("toggle-favorite-button")

    def get_favorite_count(self) -> int:
        self.favorite_count_badge.wait_for(state="visible")
        count_text = self.favorite_count_badge.inner_text()
        return int(count_text) if count_text.isdigit() else 0

    def click_favorite_button(self, title: str):
        self.get_favorite_button(title).click()

    # --- Lägg till bok/Formulär Metoder ---

    def submit_new_book(self):
        self.add_button.click()

    def get_validation_error_message(self) -> Locator:
        return self.validation_message

    def get_input_value(self, field_name: str) -> str:
        if field_name == "Titel":
            return self.title_input.input_value()
        elif field_name == "Författare":
            return self.author_input.input_value()
        else:
            raise ValueError(f"Okänt fält: {field_name}")

    def get_nav_link_by_name(self, name: str) -> Locator:
        if name == "Läslistan":
            return self.home_link
        elif name == "Mina böcker":
            return self.my_books_link
        elif name == "Lägg till bok":
            return self.add_book_link
        else:
            raise ValueError(f"Okänd navigeringslänk: {name}")

    # --- Nätverksfel Simuleringsmetod ---

    def simulate_add_book_failure(self):
        """Simulerar ett 500-fel vid POST-anrop för att lägga till bok."""
        self.page.route(
            "**/books",
            lambda route: route.fulfill(
                status=500,
                body="Simulated Server Error",
                headers={"Content-Type": "text/plain"},
            ),
        )

    def get_error_notification(self) -> Locator:
        """Returnerar lokatorn för felnotisen."""
        return self.error_notification
