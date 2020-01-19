import discord
from discord.ext import commands
from utilities import getConfig

class Social(commands.Cog, name='Social'):
    def __init__(self, bot):
        self.bot = bot
        self.config = getConfig()

    @commands.command(aliases=['s', 'social'])
    async def socialmedia(self, ctx):
        # setup
        foundAccount = False
        result = ""
        result += str(ctx.author.mention) + "\n**Socialmedia-Accounts**\n"
        result += "```"

        # check socialmedia
        if self.config['social']['linkedin'] != "":
            foundAccount = True
            result += "!linkedin|li => LinkedIn\n"
        if self.config['social']['github'] != "":
            foundAccount = True
            result += "!github|gh => GitHub\n"
        if self.config['social']['twitter'] != "":
            foundAccount = True
            result += "!twitter|tw => Twitter\n"
        if self.config['social']['instagram'] != "":
            foundAccount = True
            result += "!instagram|insta => Instagram\n"
        if self.config['social']['facebook'] != "":
            foundAccount = True
            result += "!facebook|fb => Facebook\n"
        
        #check if no account was found
        if not foundAccount:
            result += "No accounts were found"
        
        # prepare result and send result
        result += "```"

        await ctx.send(result)


    @commands.command(aliases=['li'])
    async def linkedin(self, ctx):
        if self.config['social']['linkedin'] != "":
            await ctx.send(str(ctx.author.mention) + "\n" + self.config['social']['linkedin'])

    @commands.command(aliases=['gh'])
    async def github(self, ctx):
        if self.config['social']['github'] != "":
            await ctx.send(str(ctx.author.mention) + "\n" + self.config['social']['github'])

    @commands.command(aliases=['tw'])
    async def twitter(self, ctx):
        if self.config['social']['twitter'] != "":
            await ctx.send(str(ctx.author.mention) + "\n" + self.config['social']['twitter'])

    @commands.command(aliases=['insta'])
    async def instagram(self, ctx):
        if self.config['social']['instagram'] != "":
            await ctx.send(str(ctx.author.mention) + "\n" + self.config['social']['instagram'])

    @commands.command(aliases=['fb'])
    async def facebook(self, ctx):
        if self.config['social']['facebook'] != "":
            await ctx.send(str(ctx.author.mention) + "\n" + self.config['social']['facebook'])

def setup(bot):
    bot.add_cog(Social(bot))