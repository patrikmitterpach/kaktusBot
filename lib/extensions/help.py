import discord
from discord.ext import commands
from kaktusBot import bot

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
        """

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def help(self, ctx):
        await ctx.send( helpMessage )
        return
    
def setup(bot):
    bot.add_cog(Help(bot))