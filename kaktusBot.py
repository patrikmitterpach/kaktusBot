import discord
from os import getenv
from dotenv import load_dotenv as loadDotenv


class Client (discord.Client):
    async def on_ready(self):
        print(f'{self.user} successfully connected!')

    async def on_message(self, message):
        # print(f'Registered message by {message.author}, content: \n{message.content}')
        if message.author.id == self.user.id: # Stop recursion, the bot shouldn't 
            return                            #     read its own messages

        if message.content[0] == '~':
            messageContent = message.content.split('"')
            # print(messageContent)
            if messageContent[0] == '~poll ':
                emojiReactions = ["0️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]
                # print(len(messageContent))
                pollOptions = messageContent[2][1:].split(" ")
           
                if len(pollOptions) > 7:
                    await message.channel.send(f"**Too many options for the poll!** \
                                               \n*(current maxium: {len(emojiReactions)})*")
                    return

                pollMessage = ["**Anketa:**", str(messageContent[1]), " "]
                pollMessage.extend([f'{emojiReactions[idx]}  - {char}' for idx, char in enumerate(pollOptions)])
                pollMessageString = '\n'.join(pollMessage)
                pollMessageString = pollMessageString + "\n\n"
                sentMessage = await message.channel.send(pollMessageString)
                for idx in range(len(pollOptions)):
                    await sentMessage.add_reaction(emojiReactions[idx])

            if messageContent[0] == '~pollNumbered ':
                emojiReactions = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]
                pollMessage = ["**Anketa:**", str(messageContent[1])]
                sentMessage = await message.channel.send('\n'.join(pollMessage))
                for idx in range(int(messageContent[2])):
                    await sentMessage.add_reaction(emojiReactions[idx])

loadDotenv('.env')
Client().run(getenv('discordBotToken'))