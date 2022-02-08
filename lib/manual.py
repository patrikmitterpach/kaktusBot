def helpMessage():
    helpMessage = """

**:cactus:  KAKTUSKO NÁPOVEDA  :cactus: **
Všetky sťažnosti prosím smerujte na @mitterpach#2234 , očakávam že ich bude dosť :sweat_smile:  
Zatiaľ nie je veľa dostupných príkazov, postupne budú pridávané podľa potreby.
Všetky prvky bota (vzhľad, kompozícia príkazov) sú témou debaty a nie sú určené natvrdo.

Dostupné príkazy:
**`~poll`** `"otazka ankety" moznost1 moznost2 moznost3 ...` 
- otázka musí byť vždy v úvodzovkách, možnosti iba jednoslovné
- maximum možností je 7
- použitie: `~poll "Najlepší predmet prváku?" ULI PKM TZP`

**`~pollNumbered`** `"otazka ankety" pocetMoznosti`
- vytvorí anketu s otázkou a možnosťami 1 - pocetMoznosti (max 6)
- použitie: `~pollNumbered "Koľko predmetov ste úspešne zvládli? 6`

        """

    return helpMessage