import discord
from utilities import getConfig
from discord.ext import commands

extensions = (
    'cogs.admin',
    'cogs.MainCog',
)

class UninterestingBot(commands.AutoShardedBot):
    def __init__(self):
        # get config
        self.config = getConfig()

        # setup client
        super().__init__(command_prefix=self.config['bot']['command_prefix'], case_insensitive=True)

        # remove default commands
        self.remove_command('help')
        
        # load extensions
        for extension in extensions:
            try:
                self.load_extension(extension)
            except Exception as e:
                print(e)
    
    def run(self):
        try:
            super().run(self.config['bot']['token'], reconnect=True)
        except Exception as e:
            print(e)
