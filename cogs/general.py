import discord
from discord.ext import commands
from utilities import getConfig

class General(commands.Cog, name='General'):
    def __init__(self, bot):
        self.bot = bot
        self.config = getConfig()
    
    @commands.command(aliases=['h'])
    async def help(self, ctx):
        # setup
        result = ""
        result += str(ctx.author.mention) + "\n**The following commands are available**\n"
        result += "```"

        result += "!help|h => Display this text\n\n"
        result += "!information|info|i => Show information about the bot\n\n"
        result += "!roles => Show all roles you can join\n\n"
        result += "!role|r roleA [roleB roleC...] => Join or leave a desired role (in this case roleA). Optionally, several roles (spaces separated) can be specified\n\n"
        result += "!socialmedia|social|s => Liste all linked Socialmedia accounts\n\n"
        result += "!status => Show a link to the Statuspagen"
        
        result += "```"

        # send message
        await ctx.send(result)

    @commands.command(aliases=['i', 'info'])
    async def information(self, ctx):
        # setup
        result = ""
        result += str(ctx.author.mention) + "\n"
        result += "The UninterestingBot is a self hosting Discord-Bot, written by Titus Kirch in Python.\n\n"
        result += "Website: https://uninteresting.dev\n"
        result += "Official forum: https://tkirch.dev/forum/board/25-uninterestingbot/\n"
        result += "Lexicon: https://tkirch.dev/lexicon/lexicon/34-uninterestingbot/\n"
        result += "GitHub Repository: https://github.com/TitusKirch/uninteresting-bot\n"
        result += "Website of Titus Kirch: https://tkirch.dev\n"
        result += "The official discord server of Titus Kirch: https://discord.tkirch.dev\n"

        # send message
        await ctx.send(result)

    @commands.command()
    async def status(self, ctx):
        # check if cachet url isset
        if self.config['cachet']['url'] not in ["", "myUrl"]:
            # setup
            result = ""
            result += str(ctx.author.mention) + "\n"
            result += self.config['cachet']['url']

            # send message
            await ctx.send(result)

def setup(bot):
    bot.add_cog(General(bot))