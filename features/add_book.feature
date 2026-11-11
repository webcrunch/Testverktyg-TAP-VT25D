# language: sv
Egenskap: Kataloghantering (Lägg till bok)
  Som en användare
  vill jag kunna lägga till nya böcker i katalogen
  och att formuläret rensas efteråt.

  Bakgrund:
    Givet att jag är på sidan "Läslistan"

  Scenario: Lägga till en ny bok med fullständig information OCH rensning av formuläret
    När jag navigerar till sidan "Lägg till bok"
    Och jag fyller i "Min nya titel" i fältet "Titel"
    Och jag fyller i "Anna Testare" i fältet "Författare"
    Och jag klickar på knappen "Lägg till ny bok"
    Så ska fältet "Titel" vara tomt
    Och fältet "Författare" ska vara tomt
    Och jag navigerar till sidan "Katalog"
    Så ska boken "Min nya titel" finnas i katalogen
    Och boken "Min nya titel" ska inte vara markerad som favorit

  Scenariomall: Det går inte att lägga till en bok utan att fylla i alla fält
    När jag navigerar till sidan "Lägg till bok"
    Och jag fyller i "<titel>" i fältet "Titel"
    Och jag fyller i "<författare>" i fältet "Författare"
    Så ska knappen "Lägg till ny bok" vara inaktiverad
    Och jag ska stanna kvar på sidan "Lägg till bok"

    Exempel:
      | titel       | författare      |
      |             | Kalle Testarson |
      | Bara titel  |                 |
      |             |                 |
