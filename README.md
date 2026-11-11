# Läslistan - Automatiserad Testsvit

[![Tester](https://github.com/webcrunch/Testverktyg-TAP-VT25D/actions/workflows/tests.yml/badge.svg)](https://github.com/webcrunch/Testverktyg-TAP-VT25D/actions/workflows/tests.yml)

Detta projekt innehåller en komplett testsvit för webbapplikationen "Läslistan" ([https://tap-vt25-testverktyg.github.io/exam--reading-list/](https://tap-vt25-testverktyg.github.io/exam--reading-list/)). Testerna är implementerade med Python, behave (Gherkin) och Playwright, och använder designmönstret Page Object Model (POM) för hög robusthet.

## Vad som har testats

Projektet täcker all grundläggande funktionalitet samt flera avancerade testfall (VG-nivå) för att säkerställa högsta kvalitet.

Notera att Gherkin-filerna är skrivna på svenska (Egenskap, Givet, När, Så) för att demonstrera kompetens i Gherkins flerspråkiga stöd. Varje feature-fil börjar med `# language: sv`, och `behave.ini` sätter svenska som standard.

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

* **Tillgänglighet (Accessibility):** Testar att användaren kan navigera mellan huvudlänkarna och byta vy enbart med **tangentbordet** (Tab och Enter). Att favoritmarkera en bok med tangentbordet är en känd bugg, se nedan.

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

5.  **Kör de kända buggarna:**
    ```bash
    behave --tags=bugg
    ```

## Kända buggar (`@bugg`)

Några krav i användarberättelserna uppfyller appen inte. De finns kvar som scenarier taggade `@bugg`, så att buggarna är dokumenterade och testbara, men `behave.ini` hoppar över dem i en vanlig körning. `behave --tags=bugg` kör dem, och de ska då falla.

| Scenario | Förväntat | Faktiskt |
| --- | --- | --- |
| Markera favorit med tangentbordet | Hjärtat för en bok går att nå med Tab och markera med Space | Hjärtana är `div`-element utan `tabindex` och kan inte få fokus |
| Varje vy har en huvudrubrik som matchar navigeringen | H1 är "Mina böcker" respektive "Lägg till bok" | H1 är "Läslistan" i alla vyer |

## Kontinuerlig integration

`.github/workflows/tests.yml` kör hela sviten med GitHub Actions vid varje push och pull request mot `main`, en gång i veckan (så att en ändring i appen syns även när repot står still) och för hand (Actions -> Tester -> Run workflow). Rapporten i JUnit-format sparas som artefakt i körningen.
