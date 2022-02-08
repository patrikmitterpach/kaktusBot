import discord
from discord.ext import commands

class Polls(commands.Cog):
    @commands.command
    async def poll(self, ctx, prompt, options):
        pass