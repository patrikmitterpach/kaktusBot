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
