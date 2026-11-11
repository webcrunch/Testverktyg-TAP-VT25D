# language: sv
Egenskap: Favorithantering
  Som en användare
  vill jag kunna markera och avmarkera böcker som favoriter
  så att jag snabbt kan se min personliga läslista.

  Bakgrund:
    Givet att jag är på sidan "Läslistan"

  Scenario: Markera en bok som favorit
    När jag klickar på favoritikonen för boken "Jag trodde det var tisdag"
    Och jag navigerar till sidan "Mina böcker"
    Så ska boken "Jag trodde det var tisdag" visas i listan
    Och antalet favoriter ska vara 1

  Scenario: Avmarkera en bok som favorit
    Givet att boken "Kaffekokaren som visste för mycket" är markerad som favorit
    När jag klickar på favoritikonen för boken "Kaffekokaren som visste för mycket"
    Och jag navigerar till sidan "Mina böcker"
    Så ska boken "Kaffekokaren som visste för mycket" inte visas i listan
    Och antalet favoriter ska vara 0

  Scenariomall: Upprepade klick på favoritknappen skapar inte inkonsekvens (VG)
    När jag klickar på favoritikonen för boken "<boktitel>" <antal_klick> gånger
    Och jag navigerar till sidan "Mina böcker"
    Så ska boken "<boktitel>" visas i listan om "<ska_finnas>" är "Ja"
    Och antalet favoriter ska vara <förväntat_antal_favoriter>

    Exempel:
      | boktitel             | antal_klick | ska_finnas | förväntat_antal_favoriter |
      | Min katt är min chef | 1           | Ja         | 1                         |
      | Min katt är min chef | 2           | Nej        | 0                         |
      | Min katt är min chef | 3           | Ja         | 1                         |
      | Min katt är min chef | 4           | Nej        | 0                         |

  Scenario: Favoritisera alla böcker (Maxgräns)
    När jag klickar på favoritikonen för boken "Hur man tappar bort sin TV-fjärr 10 gånger om dagen"
    Och jag klickar på favoritikonen för boken "Kaffekokaren som visste för mycket"
    Och jag klickar på favoritikonen för boken "Min katt är min chef"
    Och jag klickar på favoritikonen för boken "100 sätt att undvika måndagar"
    Och jag klickar på favoritikonen för boken "Gräv där du står – och hitta en pizzameny"
    Och jag klickar på favoritikonen för boken "Jag trodde det var tisdag"
    Och jag klickar på favoritikonen för boken "Att prata med växter – och vad de egentligen tycker om dig"
    Och jag navigerar till sidan "Mina böcker"
    Så ska boken "Hur man tappar bort sin TV-fjärr 10 gånger om dagen" visas i listan
    Och boken "Att prata med växter – och vad de egentligen tycker om dig" visas i listan
    Och antalet favoriter ska vara 7
