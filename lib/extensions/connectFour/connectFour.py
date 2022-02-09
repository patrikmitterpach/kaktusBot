import discord
from discord.ext import commands
from kaktusBot import bot
from .src.evaluation import *
from .src.graphics import drawBoard

def check(reaction, user) -> bool:
    emojiInReactions = str(reaction.emoji) in reactions
    sameMessage      = reaction.message.id == message.id
    notByBot         = user != self.bot.user

    return emojiInReactions and sameMessage and notByBot

class ConnectFour(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def connectFour(self, ctx):
        
        reactions   =   ["🇦", "🇧", "🇨", "🇩", "🇪", "🇫", "🇬"]
        gameBoard   = [ [ 0,   0,   0,   0,   0,   0,   0 ], # Scoring on the board:
                        [ 0,   0,   0,   0,   0,   0,   0 ], #    0 if Empty
                        [ 0,   0,   0,   0,   0,   0,   0 ], #    1 if Yellow
                        [ 0,   0,   0,   0,   0,   0,   0 ], #   -1 if Red
                        [ 0,   0,   0,   0,   0,   0,   0 ],
                        [ 0,   0,   0,   0,   0,   0,   0 ] ]

        turnCount = 0

        # Create an original message with coressponding emotes
        # Takes a bit of time as the bot creating reactions is slow,
        # so a loading message is displayed meanwhile
        message = await ctx.send("načítavam...")
        for reaction in reactions:
            await message.add_reaction(reaction)


        while turnCount < 42:
            string = drawBoard(gameBoard)
            await message.edit(content=string)
        
            try:
                # Get current column
                await message.add_reaction("🟡" if turnCount % 2 else "🔴")    
                
                reaction, user = await bot.wait_for("reaction_add",check=check,timeout=180)
                await message.remove_reaction(reaction, user)
                for dot in ["🟡", "🔴"]:
                    await message.remove_reaction(dot, self.bot.user)           

                currTurnColumn = reactions.index(str(reaction.emoji))
                
                # Get lowest available row                
                currTurnRow = 5
                while gameBoard[currTurnRow][currTurnColumn] != 0:
                    currTurnRow -= 1

                # Set position based on turnCount
                gameBoard[currTurnRow][currTurnColumn] = 1 if turnCount % 2 else -1
                turnCount+=1

            except IndexError:
                pass
            except TimeoutError:
                await message.edit(content="MAX ČAS NA ŤAH DOSIAHNUTÝ, HRA PRERUŠENÁ")
            
            # Check for winner
            Winner = findWinner(gameBoard)
            if Winner:
                await ctx.send(f"**VÍŤAZ:**  {'🟡' if not turnCount % 2 else '🔴'}")

        return

            
def setup(bot):
    bot.add_cog(ConnectFour(bot))