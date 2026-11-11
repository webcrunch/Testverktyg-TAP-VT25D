# language: sv
Egenskap: Tillgänglighet och Tangentbordsnavigering
  Som en användare
  vill jag kunna navigera och interagera med viktiga element via tangentbordet
  så att appen är användbar utan mus.

  Bakgrund:
    Givet att jag är på sidan "Läslistan"

  # Den aktiva vyns knapp (Katalog) är inaktiverad och hoppas därför över av Tab
  Scenario: Navigering mellan huvudlänkar med TAB
    När jag trycker på tangenten "Tab"
    Så ska navigeringslänken "Lägg till bok" ha fokus
    När jag trycker på tangenten "Tab"
    Så ska navigeringslänken "Mina böcker" ha fokus

  Scenario: Navigering till en vy med tangentbordet
    När jag trycker på tangenten "Tab" 2 gånger
    Och jag trycker på tangenten "Enter"
    Så ska navigeringslänken "Mina böcker" vara markerad som aktiv

  # Känd bugg: hjärtana är div-element utan tabindex och går inte att nå med Tab
  @bugg
  Scenario: Markera favorit med tangentbordet
    När jag tabbar till favoritikonen för boken "Min katt är min chef"
    Och jag trycker på tangenten "Space"
    Och jag navigerar till sidan "Mina böcker"
    Så ska antalet favoriter vara 1
