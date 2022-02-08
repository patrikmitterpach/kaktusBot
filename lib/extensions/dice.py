import discord
from discord.ext import commands
from random import randrange

class dice(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rtd(self, ctx):
        dice = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]
        await ctx.message.add_reaction( dice[randrange(0, 5)] )

def setup(client):
    client.add_cog(dice(client))