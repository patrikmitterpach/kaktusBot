def createPollMessage(question, options):
    emojiReactions = ["0️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
    pollMessage = ["**Anketa:**", str(question), "", "**Možnosti:**"]

    for idx, char in enumerate(options):
        pollMessage.extend([f'{emojiReactions[idx]}  - {char}'])

    pollMessageString = '\n'.join(pollMessage)

    return pollMessageString