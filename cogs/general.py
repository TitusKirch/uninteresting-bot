import discord
from discord.ext import commands

class General(commands.Cog, name='General'):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['h'])
    async def help(self, ctx):
        # setup
        result = ""
        result += "**The following commands are available**\n"
        result += "```"

        result += "!help|h => Display this text\n\n"
        result += "!information|info|i => Show information about the bot\n\n"
        result += "!roles => Show all roles you can join\n\n"
        result += "!role|r roleA [roleB roleC...] => Join or leave a desired role (in this case roleA). Optionally, several roles (spaces separated) can be specified\n\n"
        result += "!socialmedia|social|s => Liste all linked Socialmedia accounts"

        result += "```"

        # send message
        await ctx.send(result)

    @commands.command(aliases=['i', 'info'])
    async def information(self, ctx):
        await ctx.send('The UninterestingBot is a self hosting Discord-Bot, written by Titus Kirch in Python.\n\n' +
                        'Website: https://uninteresting.dev/\n' + 
                        'GitHub Repository: https://github.com/TitusKirch/uninteresting-bot\n')

def setup(bot):
    bot.add_cog(General(bot))