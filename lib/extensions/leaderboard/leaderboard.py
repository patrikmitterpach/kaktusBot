import discord
from discord.ext import commands

from .src.message import message

class Leaderboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def leaderboard(self, ctx, max=5):

        historyLimit = 10000
        messageCount = 0
        leaderBoard = {}

        async for msg in ctx.channel.history(limit=historyLimit):
                author = msg.author
                leaderBoard[author] = 1 if author not in leaderBoard else leaderBoard[author] + 1
                messageCount += 1

        print(sorted(leaderBoard.items(), key = lambda x: x[1], reverse=True))
        await ctx.send( message(leaderBoard, min(historyLimit, messageCount), max) )

        return

def setup(bot):
    bot.add_cog(Leaderboard(bot))