import discord
from discord.ext import commands
from kaktusBot import bot

from .src.manual import helpMessage

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def help(self, ctx):
        await ctx.send( helpMessage() )
        return
    
def setup(bot):
    bot.add_cog(Help(bot))