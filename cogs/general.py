import discord
from discord.ext import commands

class General(commands.Cog, name='General'):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def help(self, ctx):
        await ctx.send('>>> Coming soon')

def setup(bot):
    bot.add_cog(General(bot))