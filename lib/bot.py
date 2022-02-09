from os import listdir
from glob import glob

import discord
from discord.ext import commands
from .extensions import load 

currentGame   = 'Detroit: Become Human'
currentStatus = 'idle'
commandPrefix = '~'

# ANSI Code Colors
yellow = '\033[33m'
green = '\033[32m'
reset = '\033[m'

def logExtension(extension):
    print(f'> Loaded {green}{extension}{reset}')
class Bot(commands.Bot):
    async def on_ready(self):
        print(f'Connected as {yellow}{self.user}{reset}')

    @classmethod
    def create(cls):
        return cls(
                command_prefix = commandPrefix,
                activity       = discord.Game(currentGame),
                status         = currentStatus,
                help_command   = None )
        
    def loadExtensions(self):
        print('Loading extensions:')
        extensions = load.findExtensions('./lib/extensions/*/*.py')

        for extension in extensions:
            self.load_extension(extension) 
            logExtension(extension)
