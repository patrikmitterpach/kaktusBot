import discord
from os import getenv, system
from dotenv import load_dotenv as loadDotenv

import lib.polls as polls

system('clear')
class Client (discord.Client):
    async def on_ready(self):
        print(f'{self.user} successfully connected!')

    async def on_message(self, message):
        if message.author.id == self.user.id: # Stop recursion, the bot shouldn't 
            return                            #     read its own messages

        # Check for bot command
        if message.content[0] == '~':
            messageContent = message.content.split('"')
            
            # Create a normal poll
            if messageContent[0] == '~poll ':
                emojiReactions = ["0️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]
                pollOptions = messageContent[2][1:].split(" ")
           
                if len(pollOptions) > len(emojiReactions):
                    await message.channel.send(f"**Too many options for the poll!** \
                                               \n*(current maxium: {len(emojiReactions)})*")
                    return

                pollMessage = polls.createPollMessage(messageContent[1], pollOptions)
                sentMessage = await message.channel.send(pollMessage)
                for idx in range(len(pollOptions)):
                    await sentMessage.add_reaction(emojiReactions[idx])

            # Create a poll (answers only integers 1 up to 6)
            if messageContent[0] == '~pollNumbered ':
                emojiReactions = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]
                pollMessage = ["**Anketa:**", str(messageContent[1])]
                sentMessage = await message.channel.send('\n'.join(pollMessage))
                for idx in range(int(messageContent[2])):
                    await sentMessage.add_reaction(emojiReactions[idx])

loadDotenv('.env')
Client().run(getenv('discordBotToken'))