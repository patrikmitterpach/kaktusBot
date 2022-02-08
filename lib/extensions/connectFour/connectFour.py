import discord
from discord.ext import commands
from kaktusBot import bot
from .src.evaluation import *
class ConnectFour(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def connectFour(self, ctx):
        
        reactions   =   ["🇦", "🇧",  "🇨", "🇩", "🇪", "🇫", "🇬"]
        gameBoard   = [ [ 0,   0,   0,   0,   0,   0,   0 ], # Scoring on the board:
                        [ 0,   0,   0,   0,   0,   0,   0 ], #    0 if Empty
                        [ 0,   0,   0,   0,   0,   0,   0 ], #    1 if Yellow
                        [ 0,   0,   0,   0,   0,   0,   0 ], #   -1 if Red
                        [ 0,   0,   0,   0,   0,   0,   0 ],
                        [ 0,   0,   0,   0,   0,   0,   0 ] ]

        positions = {  -1: "  🔴  ",
                        0: "          ",
                        1: "  🟡  " }
        turnCount = 0

        message = await ctx.send("načítavam...")
        for reaction in reactions:
            await message.add_reaction(reaction)
        while turnCount < 42:
            print(f'turn: {turnCount}')
            string = "**-------------                 CONNECT 4                 -------------**\n\n"
            string += "\t\t *Pre zvolenie stĺpca stlačte príslušnú reakciu.*\n\t *Ťah možno spraviť len ak je indikovaná ikonka\n\t\t\t\t\t\t\t\t súčasného ťahu*\n\n"
            for i in range(len(gameBoard)):
                string += '   '
                for ii in range(len(gameBoard[0]) - 1):
                    string += f'{positions[gameBoard[i][ii]]} | '
                string += f'{positions[gameBoard[i][6]]}\n'
            string += "▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\n\t"

            await message.edit(content=string)

            def check(reaction, user) -> bool:
                return str(reaction.emoji) in reactions and reaction.message.id == message.id and user != self.bot.user

            try:
                await message.add_reaction("🟡" if turnCount % 2 else "🔴")    
                reaction, user = await bot.wait_for("reaction_add",check=check,timeout=180)
                await message.remove_reaction(reaction, user)
                
                for dot in ["🟡", "🔴"]:
                    await message.remove_reaction(dot, self.bot.user)           
                currTurnRow = 5
                currTurnColumn = reactions.index(str(reaction.emoji))

                while gameBoard[currTurnRow][currTurnColumn] != 0:
                    currTurnRow -= 1

                gameBoard[currTurnRow][currTurnColumn] = 1 if turnCount % 2 else -1
                await message.edit(content=string)
                turnCount+=1
            except IndexError:
                pass
            Winner = findWinner(gameBoard)
            if Winner:
                await ctx.send(f"**VÍŤAZ:** {' 🟡' if not turnCount % 2 else ' 🔴'}")

        return

            
def setup(bot):
    bot.add_cog(ConnectFour(bot))