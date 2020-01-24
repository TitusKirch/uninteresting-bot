import discord
import logging
from datetime import datetime
from utilities import getConfig
from discord.ext import commands
from models.setting import Setting
from db import db_session

class UninterestingBot(commands.AutoShardedBot):
    def __init__(self):
        # get config
        self.config = getConfig()

        # setup logger if logging is true
        if(self.config['bot']['logging'] == 'true'):
            # get loggers
            self.discordLogger = logging.getLogger('discord')
            self.sqlalchemyLogger = logging.getLogger('sqlalchemy.engine')

            # set debug levels
            self.discordLogger.setLevel((logging.DEBUG if self.config['bot']['debug'] == 'true' else logging.ERROR))
            self.sqlalchemyLogger.setLevel((logging.DEBUG if self.config['bot']['debug'] == 'true' else logging.ERROR))
            
            # setup handler
            handler = logging.FileHandler(filename=datetime.now().strftime('logs/log%Y-%m-%d_%H-%M-%S.log'), encoding='utf-8', mode='w')
            handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))

            # add handlers
            self.discordLogger.addHandler(handler)
            self.sqlalchemyLogger.addHandler(handler)

        # setup client
        super().__init__(command_prefix=self.config['bot']['command_prefix'], case_insensitive=True)
    
    async def on_ready(self):
        # log logged in if logging is true
        if(self.config['bot']['logging'] == 'true'):
            self.discordLogger.info('Logged in as "' + self.user.name + '" [ID: ' + str(self.user.id) + ']')

        # set presence
        await self.change_presence(activity=discord.Activity(
            name=Setting.get('status_name'),
            type=discord.ActivityType.playing))
    
    def run(self):
        # try to run bot
        try:
            # print for debug
            print('Bot is starting')

            # run bot
            super().run(self.config['bot']['token'], reconnect=True)

        except Exception:
            # print for debug
            print('Bot stopped')

            # close bot
            self.close()

            # log exception if logging is true
            if(self.config['bot']['logging'] == 'true'):
                self.discordLogger.exception('Bot run exception')
