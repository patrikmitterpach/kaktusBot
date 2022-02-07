def createPollMessage(question, options):
    emojiReactions = ["0️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]
    pollMessage = ["**Anketa:**", str(question)]

    for idx, char in enumerate(options):
        pollMessage.extend([f'{emojiReactions[idx]}  - {char}'])

    pollMessageString = '\n'.join(pollMessage)

    return pollMessageString