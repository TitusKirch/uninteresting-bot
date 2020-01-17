import discord
import logging
from datetime import datetime
from utilities import getConfig
from discord.ext import commands

extensions = (
    'cogs.admin',
    'cogs.general',
    'cogs.members',
    'cogs.rules'
)

class UninterestingBot(commands.AutoShardedBot):
    def __init__(self):
        # get config
        self.config = getConfig()

        #setup logger if logging is true
        if(self.config['bot']['logging'].lower() == 'true'):
            logger = logging.getLogger('discord')
            logger.setLevel((logging.DEBUG if self.config['bot']['debug'].lower() == 'true' else logging.ERROR))
            handler = logging.FileHandler(filename=datetime.now().strftime('logs/log%Y-%m-%d_%H-%M-%S.log'), encoding='utf-8', mode='w')
            handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
            logger.addHandler(handler)

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
        if self.config['bot']['status_name'] != '':
            await self.change_presence(activity=discord.Activity(
                name=self.config['bot']['status_name'],
                type=discord.ActivityType.playing))
        print('Logged in as "' + self.user.name + '" [ID: ' + str(self.user.id) + ']')
    
    def run(self):
        try:
            super().run(self.config['bot']['token'], reconnect=True)
        except Exception as e:
            print(e)
