# language: sv
Egenskap: Navigering och Appstruktur
  Som en användare
  vill jag kunna navigera smidigt mellan vyerna
  och alltid veta var jag befinner mig.

  Bakgrund:
    Givet att jag är på sidan "Läslistan"

  Scenario: Verifiera startsidans grundläggande struktur och navigationsindikator
    Så ska webbläsarfönstrets titel vara "Läslistan"
    Och sidans huvudrubrik (H1) ska vara "Läslistan"
    Och navigeringslänken "Katalog" ska vara markerad som aktiv

  Scenario: Navigering till Mina böcker och visuell indikering
    När jag navigerar till sidan "Mina böcker"
    Så ska navigeringslänken "Mina böcker" vara markerad som aktiv
    Och navigeringslänken "Katalog" ska inte vara markerad som aktiv

  Scenario: Navigering till Lägg till bok och visuell indikering
    När jag navigerar till sidan "Lägg till bok"
    Så ska navigeringslänken "Lägg till bok" vara markerad som aktiv

  # Känd bugg: rubriken är "Läslistan" i alla vyer, inte vyns namn
  @bugg
  Scenariomall: Varje vy har en huvudrubrik som matchar navigeringen
    När jag navigerar till sidan "<vy>"
    Så ska sidans huvudrubrik (H1) vara "<vy>"

    Exempel:
      | vy            |
      | Mina böcker   |
      | Lägg till bok |
