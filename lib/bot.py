from os import system

import discord
from discord.ext import commands


currentGame   = 'Detroit: Become Human'
currentStatus = 'idle'
commandPrefix = '~'


class Bot(commands.Bot):
    @classmethod
    def create(cls):
        system('clear')
        print(f'{Bot.user.name} connection created.')
        return cls(
            command_prefix = commandPrefix,
            activity = discord.Game(currentGame),
            status = currentStatus,
            help_command=None)
    
    def loadExtensions(self):
        extensionList = [ 'lib.extensions.help',
                          'lib.extensions.ping' ]
        for extension in extensionList:
            self.load_extension(extension)
            print(f'Loaded {extension}')