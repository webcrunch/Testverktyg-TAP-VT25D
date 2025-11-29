Feature: Felhantering och Robusthet
    Som en användare
    vill jag få tydlig återkoppling om nätverksåtgärder misslyckas
    så att jag förstår varför en handling inte genomfördes.

    Background:
    Givet att jag är på sidan "Läslistan"

    Scenario: Systemet hanterar misslyckat tillägg av bok (Simulerat Nätverksfel)
Givet att servern är nere och ger felkod 500 vid försök att lägga till bok
När jag navigerar till sidan "Lägg till bok"
Och jag fyller i "Misslyckad bok" i fältet "Titel"
Och jag fyller i "Misslyckad Författare" i fältet "Författare"
Och jag klickar på knappen "Lägg till"
Så ska ett felmeddelande visas för nätverksfelet
Och boken "Misslyckad bok" ska inte finnas i katalogen