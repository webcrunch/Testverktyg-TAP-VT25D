Feature: Kataloghantering (Lägg till bok)
    Som en användare
    vill jag kunna lägga till nya böcker i katalogen
    och att formuläret rensas efteråt.

    Background:
    Givet att jag är på sidan "Läslistan"

    Scenario: Lägga till en ny bok med fullständig information OCH rensning av formuläret
    När jag navigerar till sidan "Lägg till bok"
    Och jag fyller i "Min nya titel" i fältet "Titel"
    Och jag fyller i "Anna Testare" i fältet "Författare"
    Och jag klickar på knappen "Lägg till"
    Så ska fältet "Titel" vara tomt
    Och fältet "Författare" ska vara tomt
    Och jag navigerar till sidan "Läslistan"
    Så ska boken "Min nya titel" finnas i katalogen
    Och boken "Min nya titel" ska inte vara markerad som favorit

    Scenario: Felhantering vid försök att lägga till bok utan titel
När jag navigerar till sidan "Lägg till bok"
Och jag fyller i "Kalle Testarson" i fältet "Författare"
Och jag lämnar fältet "Titel" tomt
Och jag klickar på knappen "Lägg till"
Så ska ett felmeddelande visas för fältet "Titel"
Och jag ska stanna kvar på sidan "Lägg till bok"