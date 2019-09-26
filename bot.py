import discord
from utilities import getConfig
from discord.ext import commands
from cogs.MainCog import MainCog as MainCog

def run():
    # get config
    config = getConfig()

    # create client
    client = commands.Bot(command_prefix=config['bot']['command_prefix'], case_insensitive=True)
    client.add_cog(MainCog(client))
    client.run(config['bot']['token'])



