Feature: Persistens och Session
    Som en användare
    vill jag veta att mitt tillstånd är flyktigt
    så att jag kan rensa mina favoriter och börja om genom att ladda om sidan.

    Background:
    Givet att jag är på sidan "Läslistan"

    Scenario: Nyligen tillagd bok ska försvinna vid omladdning
    Givet att jag har lagt till boken "Flyktig Titel" av "Flyktig Författare" i katalogen
    När jag laddar om sidan
    Och jag navigerar till sidan "Läslistan"
    Så ska boken "Flyktig Titel" inte finnas i katalogen
    Och antalet favoriter ska vara 3

    Scenario: Favoritmarkeringar ska försvinna vid omladdning
Givet att boken "Hur man tappar bort sin TV-fjärr 10 gånger om dagen" är markerad som favorit
När jag laddar om sidan
Och jag navigerar till sidan "Mina böcker"
Så ska boken "Hur man tappar bort sin TV-fjärr 10 gånger om dagen" inte visas i listan
Och antalet favoriter ska vara 3