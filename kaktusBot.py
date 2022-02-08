import discord
from os import getenv, system
from dotenv import load_dotenv as loadDotenv

import lib.polls as polls
import lib.manual as manual
from lib.bot import Bot 

loadDotenv('.env')
token = getenv('discordBotToken')


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

#         if message.content[0] == '~':
#             command = message.content.split()[0][1:] # first word without the first char (~)
#             print(f'{message.author} used {command} in {message.channel}')
            
#             if command == 'help':
#                 await message.channel.send( manual.helpMessage() )

#             # Create a normal poll
#             elif command == 'poll':
#                 messageContent = message.content.split('"')
#                 emojiReactions = ["0️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]
#                 pollOptions = messageContent[2][1:].split(" ")
           
#                 if len(pollOptions) > len(emojiReactions):
#                     await message.channel.send(f"**Too many options for the poll!** \
#                                                \n*(current maxium: {len(emojiReactions)})*")
#                     return

#                 pollMessage = polls.createPollMessage(messageContent[1], pollOptions)
#                 sentMessage = await message.channel.send(pollMessage)
#                 for idx in range(len(pollOptions)):
#                     await sentMessage.add_reaction(emojiReactions[idx])

#             # Create a poll (answers only integers 1 up to 6)
#             elif command == 'pollNumbered':
#                 messageContent = message.content.split('"')
#                 emojiReactions = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]
#                 pollMessage = ["**Anketa:**", str(messageContent[1])]
#                 sentMessage = await message.channel.send('\n'.join(pollMessage))
#                 for idx in range(int(messageContent[2])):
#                     await sentMessage.add_reaction(emojiReactions[idx])

