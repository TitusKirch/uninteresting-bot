import discord
from utilities import getConfig
from discord.ext import commands

extensions = (
    'cogs.admin',
    'cogs.MainCog',
)

def run():
    # get config
    config = getConfig()

    # create client
    client = commands.Bot(command_prefix=config['bot']['command_prefix'], case_insensitive=True)

    # remove default commands
    client.remove_command('help')

    # load extensions
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            print(e)

    # run bot
    client.run(config['bot']['token'])