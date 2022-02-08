import discord
from discord.ext import commands
from .src.polls import createPollMessage

class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def poll(self, ctx, prompt, *options):
        reactions = ["0️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
        maxPollLength = len(reactions)

        if len(options) > maxPollLength:
            await ctx.send(f"**Príliš veľa možností!**\n*(súčasné maximum: {len(reactions)})*")
            return

        pollMessage = createPollMessage(prompt, options)

        sentMessage = await ctx.send(pollMessage)
        for idx in range(len(options)):
            await sentMessage.add_reaction(reactions[idx])
        return
    
def setup(bot):
    bot.add_cog(Poll(bot))