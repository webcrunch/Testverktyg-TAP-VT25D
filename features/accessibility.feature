Feature: Tillgänglighet och Tangentbordsnavigering
    Som en användare
    vill jag kunna navigera och interagera med viktiga element via tangentbordet
    så att appen är användbar utan mus.

    Scenario: Navigering mellan huvudlänkar med TAB
    Givet att jag är på sidan "Läslistan"
    När jag trycker på tangenten "Tab"
    Så ska navigeringslänken "Läslistan" ha fokus
    När jag trycker på tangenten "Tab"
    Så ska navigeringslänken "Mina böcker" ha fokus
    När jag trycker på tangenten "Tab"
    Så ska navigeringslänken "Lägg till bok" ha fokus

    Scenario: Markera favorit med tangentbordet
Givet att jag är på sidan "Läslistan"
När jag trycker på tangenten "Tab" 10 gånger # Tabba förbi navigeringslänkar och första böckerna
Och jag trycker på tangenten "Space"
Och jag navigerar till sidan "Mina böcker"
Så ska antalet favoriter vara 4