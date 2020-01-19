import discord
import logging
from datetime import datetime
from utilities import getConfig
from discord.ext import commands
import asyncio
import requests

extensions = (
    'cogs.admin',
    'cogs.general',
    'cogs.members',
    'cogs.rules',
    'cogs.specialroles',
    'cogs.social'
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
    
        # check if cachet url isset
        if self.config['cachet']['url'] not in ["", "myUrl"]:
            # check if api_token isset
            if self.config['cachet']['api_token'] not in ["", "myToken"]:
                # check component id
                if int(self.config['cachet']['component_id']) > 0:
                    # loop status
                    self.loop.create_task(self.cachet_status())
    
    async def cachet_status(self):
        while True:
            try:
                headers = {'content-type': 'application/json', 'X-Cachet-Token': self.config['cachet']['api_token'], 'User-Agent': 'Mozilla/5.0'}
                payload = "{\"status\": " + str(1) + ", \"meta\":{\"time\": \"" + str(int(datetime.timestamp(datetime.now()))) + "\"}}"
                path = "/api/v1/components/" + self.config['cachet']['component_id']
                requests.request("PUT", self.config['cachet']['url'] + path, data=payload, headers=headers)
            except:
                pass
            await asyncio.sleep(int(self.config['cachet']['interval']))
    
    def run(self):
        try:
            super().run(self.config['bot']['token'], reconnect=True)
        except Exception as e:
            print(e)
