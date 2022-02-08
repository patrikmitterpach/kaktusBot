import discord
from os import getenv, system
from dotenv import load_dotenv as loadDotenv

import lib.polls as polls
import lib.manual as manual
from lib.bot import Bot 

loadDotenv('.env')
token = getenv('discordBotToken')

system('clear')

bot = Bot.create()
bot.loadExtensions()
bot.run(token)

# class Client (discord.Client):
#     async def on_ready(self):
#         system('clear')
#         print(f'{self.user} successfully connected!')
#         await self.change_presence(status="idle",\
#                                    activity=discord.Game("Detroit: Become Human"))

#     async def on_message(self, message):
#         # Ignore messages created by the bot
#         if message.author.id == self.user.id: 
#             return                            

#             # Create a poll (answers only integers 1 up to 6)
#             elif command == 'pollNumbered':
#                 messageContent = message.content.split('"')
#                 emojiReactions = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]
#                 pollMessage = ["**Anketa:**", str(messageContent[1])]
#                 sentMessage = await message.channel.send('\n'.join(pollMessage))
#                 for idx in range(int(messageContent[2])):
#                     await sentMessage.add_reaction(emojiReactions[idx])

