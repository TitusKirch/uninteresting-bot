import discord
from utilities import _
from discord.ext import commands
from models.extension import Extension

class General(commands.Cog, name='General'):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['i', 'info'])
    async def information(self, ctx):
        # create output embed
        embed = discord.Embed(
            colour = discord.Colour.blue(),
            title = _("information"),
            description = _("bot description")
        )
        embed.add_field(name=_("website"), value="https://uninteresting.dev", inline=False)
        embed.add_field(name=_("forum"), value="https://tkirch.dev/forum/board/25-uninterestingbot/", inline=False)
        embed.add_field(name=_("lexicon"), value="https://tkirch.dev/lexicon/lexicon/34-uninterestingbot/", inline=False)
        embed.add_field(name=_("github repository"), value="https://github.com/TitusKirch/uninteresting-bot", inline=False)
        embed.add_field(name=_("website tkirch"), value="https://tkirch.dev", inline=False)
        embed.add_field(name=_("discord tkirch"), value="https://discord.tkirch.dev", inline=False)
        
        # send message
        await ctx.send(ctx.author.mention, embed=embed)
    
    @commands.command(aliases=['h'])
    async def help(self, ctx):
        # create output embed
        embed = discord.Embed(
            colour = discord.Colour.blue(),
            title = _("help"),
            description = _("help description")
        )
        embed.add_field(name="!i|info|information", value=_("information help"), inline=False)
        embed.add_field(name="!h|help", value=_("help help"), inline=False)

        if any(extension.name == "fun" for extension in Extension.loaded()):
            embed.add_field(name="!dice", value=_("dice help"), inline=False)
        
        # send message
        await ctx.send(ctx.author.mention, embed=embed)

def setup(bot):
    bot.add_cog(General(bot))