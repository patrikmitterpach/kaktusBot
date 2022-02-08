import discord
from os import getenv, system
from dotenv import load_dotenv as loadDotenv

from lib.bot import Bot 

loadDotenv('.env')
token = getenv('discordBotToken')

system('clear')

bot = Bot.create()
bot.loadExtensions()
bot.run(token)
