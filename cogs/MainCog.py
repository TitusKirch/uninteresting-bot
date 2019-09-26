import discord
from discord.ext import commands
from utilities import getConfig

class MainCog(commands.Cog, name='MainCog'):
    def __init__(self, bot):
        self.bot = bot
        self.config = getConfig()

    @commands.Cog.listener()
    async def on_ready(self):
        if self.config['bot']['game_name'] != '':
            await self.bot.change_presence(activity=discord.Activity(name=self.config['bot']['game_name'], type=discord.ActivityType.playing))
        print('Logged in as "' + self.bot.user.name + '" [ID: ' + str(self.bot.user.id) + ']')