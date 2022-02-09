from os import listdir
from glob import glob

import discord
from discord.ext import commands
from .extensions import load 

currentGame   = 'Detroit: Become Human'
currentStatus = 'idle'
commandPrefix = '~'

# ANSI Code Colors
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'

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
        # Extensions are assumed to be placed in /lib/extensions/name/name.py,
        #   where name is the name of the extension.

        print('Loading extensions:')
        extensionPath = './lib/extensions/*/*.py' # regex for finding all modules
        extensions = load.findExtensions(extensionPath)

        errCount = 0
        fullCount = len(extensions)

        for extension in extensions:
            try:
                self.load_extension(extension) 
                logExtension(extension)
            except commands.NoEntryPointError:
                print(f"{red}{extension}{reset} has no setup function.")
                errCount += 1
        
        print(f"(Loaded {fullCount - errCount}/{fullCount} extensions)")