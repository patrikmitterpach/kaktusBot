def helpMessage():
    helpMessage = "\
**:cactus:  KAKTUSKO NÁPOVEDA  :cactus: ** \n\
Všetky sťažnosti prosím smerujte na @mitterpach#2234 , očakávam že ich bude dosť :sweat_smile: \n\
Zatiaľ nie je veľa dostupných príkazov, postupne budú pridávané podľa potreby. \n\
Všetky prvky bota (vzhľad, kompozícia príkazov) sú témou debaty a nie sú určené natvrdo. \n\
\n\
**Dostupné príkazy:**\n\
**`~poll`** `\"otazka ankety\" moznost1 moznost2 moznost3 ...` \n\
- otázka musí byť vždy v úvodzovkách, možnosti iba jednoslovné \n\
- maximum možností je 7 \n\
- použitie: `~poll \"Najlepší predmet prváku?\" ULI PKM TZP` \n\
\n\
**`~pollNumbered`** `\"otazka ankety\" pocetMoznosti`\n\
- vytvorí anketu s otázkou a možnosťami 1 - pocetMoznosti (max 6)\n\
- použitie: `~pollNumbered \"Koľko predmetov ste úspešne zvládli?\" 6`"

    return helpMessage