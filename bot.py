import discord
from utilities import getConfig
from discord.ext import commands

extensions = (
    'cogs.admin',
    'cogs.general',
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
    
    async def on_ready(self):
        if self.config['bot']['game_name'] != '':
            await self.change_presence(activity=discord.Activity(name=self.config['bot']['game_name'], type=discord.ActivityType.playing))
        print('Logged in as "' + self.user.name + '" [ID: ' + str(self.user.id) + ']')
    
    def run(self):
        try:
            super().run(self.config['bot']['token'], reconnect=True)
        except Exception as e:
            print(e)
