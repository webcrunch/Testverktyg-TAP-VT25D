Feature: Favorithantering
    Som en användare
    vill jag kunna markera och avmarkera böcker som favoriter
    så att jag snabbt kan se min personliga läslista.

    Background:
    Givet att jag är på sidan "Läslistan"

    Scenario: Markera en bok som favorit
    När jag klickar på favoritikonen för boken "Pippi Långstrump"
    Och jag navigerar till sidan "Mina böcker"
    Så ska boken "Pippi Långstrump" visas i listan
    Och antalet favoriter ska vara 4

    Scenario: Avmarkera en bok som favorit
    Givet att boken "Kaffekokaren som visste för mycket" är markerad som favorit
    När jag klickar på favoritikonen för boken "Kaffekokaren som visste för mycket"
    Och jag navigerar till sidan "Mina böcker"
    Så ska boken "Kaffekokaren som visste för mycket" inte visas i listan
    Och antalet favoriter ska vara 2

    Scenario Outline: Upprepade klick på favoritknappen skapar inte inkonsekvens (VG)
            När jag klickar på favoritikonen för boken "<boktitel>" <antal_klick> gånger
            Och jag navigerar till sidan "Mina böcker"
            Så ska boken "<boktitel>" visas i listan om "<ska_finnas>" är "Ja"
            Och antalet favoriter ska vara <förväntat_antal_favoriter>

            Exempel:
            | boktitel             | antal_klick | ska_finnas | förväntat_antal_favoriter |
            | Min katt är min chef | 1           | Ja         | 4                         |
            | Min katt är min chef | 2           | Nej        | 3                         |
            | Min katt är min chef | 3           | Ja         | 4                         |
            | Min katt är min chef | 4           | Nej        | 3                         |


    Scenario: Favoritisera alla böcker (Maxgräns)
Givet att jag är på sidan "Läslistan"
När jag klickar på favoritikonen för boken "Hur man tappar bort sin TV-fjärr 10 gånger om dagen"
Och jag klickar på favoritikonen för boken "Kaffekokaren som visste för mycket"
Och jag klickar på favoritikonen för boken "Min katt är min chef"
Och jag klickar på favoritikonen för boken "100 sätt att undvika måndagar"
Och jag klickar på favoritikonen för boken "Gräv där du står – och hitta en pizzameny"
Och jag navigerar till sidan "Mina böcker"
Så ska boken "Hur man tappar bort sin TV-fjärr 10 gånger om dagen" visas i listan
Och boken "Gräv där du står – och hitta en pizzameny" visas i listan
Och antalet favoriter ska vara 7