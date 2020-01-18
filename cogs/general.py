import discord
from discord.ext import commands

class General(commands.Cog, name='General'):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['h'])
    async def help(self, ctx):
        await ctx.send('>>> Coming soon')

    @commands.command(aliases=['i'])
    async def info(self, ctx):
        await ctx.send('The UninterestingBot is a self hosting Discord-Bot, written by Titus Kirch in Python.\n\n' +
                        'Website: https://uninteresting.dev/\n' + 
                        'GitHub Repository: https://github.com/TitusKirch/uninteresting-bot\n')

def setup(bot):
    bot.add_cog(General(bot))