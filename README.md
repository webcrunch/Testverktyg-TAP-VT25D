# Läslistan - Automatiserad Testsvit 

Detta projekt innehåller en komplett testsvit för webbapplikationen "Läslistan" ([https://tap-vt25-testverktyg.github.io/exam--reading-list/](https://tap-vt25-testverktyg.github.io/exam--reading-list/)). Testerna är implementerade med Python, behave (Gherkin) och Playwright, och använder designmönstret Page Object Model (POM) för hög robusthet.

## Vad som har testats

Projektet täcker all grundläggande funktionalitet samt flera avancerade testfall (VG-nivå) för att säkerställa högsta kvalitet.

"Notera att Gherkin-filerna är skrivna på svenska (Givet, När, Så) för att demonstrera kompetens i Gherkins flerspråkiga stöd."

### Grundfunktionalitet (G)

* **Favorithantering:** Markera, avmarkera och räkna favoriter.
* **Kataloghantering:** Lägga till nya böcker i katalogen.
* **Navigering & Vyer:** Korrekt sidtitel (<title>), huvudrubrik (H1) och visuell indikering av aktiv navigeringslänk.

### Utökad Kvalitet (VG)

* **Page Object Model (POM):** Används genomgående i strukturen (`pages/`) för återanvändbarhet och robusthet.
* **Scenario Outline:** Används för att effektivt testa **upprepade klick på favoritknappen** (t.ex. klick 1, 2, 3, 4) för att säkerställa att tillståndet är konsekvent.
* **Validering & Felhantering:**
    * Testar att användaren **inte** kan lägga till en bok utan att fylla i alla obligatoriska fält.
    * Testar att **formulärfälten rensas** automatiskt efter ett framgångsrikt tillägg (bra UX).
    * Testar **nätverksfel** genom att simulera ett HTTP 500-fel (server error) vid försök att lägga till en bok, och verifierar att ett användarvänligt felmeddelande visas.
* **Persistens:** Testar att alla flyktiga ändringar (nyligen tillagda böcker och favoritmarkeringar) **försvinner** efter att sidan laddas om, vilket bekräftar appens sessionsbaserade natur.

## Hur man startar projektet

### Förutsättningar

* Python 3.8+
* Git installerat

### Steg

1.  **Klona repositoryt:**
    ```bash
    git clone git@github.com:webcrunch/Testverktyg-TAP-VT25D.git
    cd Testverktyg-TAP-VT25D
    ```

2.  **Aktivera virtuell miljö (Bash/Git Bash):**
    ```bash
    source .venv/Scripts/activate
    ```

3.  **Installera beroenden:**
    ```bash
    pip install -r requirements.txt
    playwright install
    ```

4.  **Kör hela testsviten:**
    ```bash
    behave
    ```
    *(Testerna körs i headless-läge som standard för snabbhet.)*
