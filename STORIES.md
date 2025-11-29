## 📜 Sammanfattad Lista över User Stories (Korrigerad)
### 1. Favoritfunktioner och Tillstånd
- Som användare vill jag kunna markera en bok som favorit så att jag snabbt hittar den senare på sidan Mina böcker.

- Som användare vill jag kunna avmarkera en favorit så att min favoritlista hålls uppdaterad.

- Som användare vill jag att upprepade klick på favoritknappen inte skapar inkonsekvens så att listan förblir korrekt. (VG: Scenario Outline)

- Som användare vill jag kunna favoritisera alla böckerna och få en lista på de sju som är default från början. (Testar maxgräns)

### 2. Kataloghantering och Validering
- Som användare vill jag kunna lägga till en ny bok i katalogen så att jag kan spara titlar som saknas.

- Som användare vill jag inte kunna lägga till en bok utan att ha fyllt i alla fälten. (Felhantering/Validering)

- Som användare vill jag se att fälten rensas automatiskt efter att jag har lagt till en ny bok. (UX-test)

### 3. Navigering och Vyer
- Som användare vill jag att aktuell vy indikeras visuellt så att jag vet var jag befinner mig i appen.

- Som användare vill jag att webbläsarfönstrets titel ska vara korrekt för den aktuella sidan (<title>).

- Som användare vill jag att varje vy har en tydlig huvudrubrik (H1) som matchar navigationen, så att jag omedelbart vet vilken sida jag har landat på. (Ersätter H1-kravet)

### 4. Persistens och Session
- Som användare vill jag kunna återställa eller rensa mina favoriter så att jag kan börja om vid behov (genom att ladda om sidan). (Testar flyktigt tillstånd)

### 5. Avancerad Felhantering och Robusthet (VG)
- Som användare vill jag att systemet hanterar nätverksfel graciöst så att jag får återkoppling när åtgärder misslyckas. (VG: Nätverksmockning)

### 6. Kvalitetskrav (Kortfattat)
- Som testare vill jag ha stabila selectors för UI‑element så att automatiserade tester är robusta.

- Som användare vill jag att viktiga funktioner är åtkomliga via tangentbord så att appen är användbar utan mus.