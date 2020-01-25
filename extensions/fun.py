import discord
import random
from utilities import _
from discord.ext import commands

class Fun(commands.Cog, name='Fun'):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def dice(self, ctx):
        await ctx.send(_("dice role, {mention}, {dice}").format(mention=ctx.author.mention, dice=random.randint(1,6)))

def setup(bot):
    bot.add_cog(Fun(bot))