from os import listdir

import discord
from discord.ext import commands


currentGame   = 'Detroit: Become Human'
currentStatus = 'idle'
commandPrefix = '~'

# colors
yellow = '\033[33m'
green = '\033[32m'
reset = '\033[m'


class Bot(commands.Bot):
    async def on_ready(self):
        print(f'Connected as {yellow}{self.user}{reset}')

    @classmethod
    def create(cls):
        return cls(
                command_prefix = commandPrefix,
                activity = discord.Game(currentGame),
                status = currentStatus,
                help_command=None )
        
    def loadExtensions(self):
        print('Loading extensions:')
        for filename in listdir('./lib/extensions'): #loads all files (*.py)
            if filename.endswith('.py'):
                self.load_extension(f'lib.extensions.{filename[:-3]}') #loads the file without ".py" 
                print(f'> Loaded {green}{filename[:-3]}{reset} from lib.extensions.{filename[:-3]}')
