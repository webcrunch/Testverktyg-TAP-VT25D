Feature: Navigering och Appstruktur
  Som en användare
  vill jag kunna navigera smidigt mellan vyerna
  och alltid veta var jag befinner mig.

  Background:
  Givet att jag är på sidan "Läslistan"

  Scenario: Verifiera startsidans grundläggande struktur och navigationsindikator
  Så ska webbläsarfönstrets titel vara "Läslistan"
  Och sidans huvudrubrik (H1) ska vara "Läslistan"
  Och navigeringslänken "Läslistan" ska vara markerad som aktiv

  Scenario: Navigering till Mina böcker och visuell indikering
  När jag navigerar till sidan "Mina böcker"
  Så ska navigeringslänken "Mina böcker" vara markerad som aktiv
  Och sidans huvudrubrik (H1) ska vara "Mina Böcker"

  Scenario: Navigering till Lägg till bok och visuell indikering
När jag navigerar till sidan "Lägg till bok"
Så ska navigeringslänken "Lägg till bok" vara markerad som aktiv
Och sidans huvudrubrik (H1) ska vara "Lägg till bok"