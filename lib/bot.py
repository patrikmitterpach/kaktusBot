from os import listdir
from glob import glob

import discord
from discord.ext import commands

currentGame   = 'Detroit: Become Human'
currentStatus = 'idle'
commandPrefix = '~'

# ANSI Code Colors
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

        for filename in glob('./lib/extensions/*/*.py'):
            module = filename.split('/')[-1] #loads all files (*.py)
            self.load_extension(f'lib.extensions.{module[:-3]}.{module[:-3]}') # [:-3] to remove '.py' 
            print(f'> Loaded {green}{module[:-3]}{reset} from lib.extensions.{module[:-3]}.')
