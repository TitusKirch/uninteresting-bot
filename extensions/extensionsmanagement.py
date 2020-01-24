import discord
from utilities import _
from discord.ext import commands

class ExtensionsManagement(commands.Cog, name='ExtensionsManagement'):
    def __init__(self, bot):
        self.bot = bot
        self.extensions_dir = 'extensions.'
        self.extension_blacklist = [
            'extensionsmanagement' 
        ]
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def load(self, ctx, extension: str):
        # prepare extension string
        extension = extension.lower()

        # check if extension is not on blacklist
        if extension not in self.extension_blacklist:

            # try to load extension
            try:
                self.bot.load_extension(self.extensions_dir + extension)
            except Exception as e:
                # create output embed
                embed = discord.Embed(
                    colour = discord.Colour.red(),
                    title = _("extension not loaded, {extension}").format(extension=extension)
                )
                embed.add_field(name=_("Errors"), value="{}: {}".format(type(e).__name__, e), inline=False)

                # send embed
                await ctx.send(embed=embed)
            else:
                # create output embed
                embed = discord.Embed(
                    colour = discord.Colour.green(),
                    title = _("extension successfully loaded, {extension}").format(extension=extension)
                )
                # send embed
                await ctx.send(embed=embed)
        else:
            # create output embed
            embed = discord.Embed(
                colour = discord.Colour.red(),
                title = _("extension not loaded, {extension}").format(extension=extension)
            )
            embed.add_field(name=_("Errors"), value=_("extension blacklist"), inline=False)

            # send embed
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unload(self, ctx, extension : str):
        # prepare extension string
        extension = extension.lower()

        # check if extension is not on blacklist
        if extension not in self.extension_blacklist:
            # try to unload extension
            try:
                self.bot.unload_extension(self.extensions_dir + extension)
            except Exception as e:
                # create output embed
                embed = discord.Embed(
                    colour = discord.Colour.red(),
                    title = _("extension not unloaded, {extension}").format(extension=extension)
                )
                embed.add_field(name=_("Errors"), value="{}: {}".format(type(e).__name__, e), inline=False)

                # send embed
                await ctx.send(embed=embed)
            else:
                # create output embed
                embed = discord.Embed(
                    colour = discord.Colour.green(),
                    title = _("extension successfully unloaded, {extension}").format(extension=extension)
                )
                # send embed
                await ctx.send(embed=embed)
        else:
            # create output embed
            embed = discord.Embed(
                colour = discord.Colour.red(),
                title = _("extension not unloaded, {extension}").format(extension=extension)
            )
            embed.add_field(name=_("Errors"), value=_("extension blacklist"), inline=False)

            # send embed
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx, extension : str):
        # prepare extension string
        extension = extension.lower()

        # check if extension is not on blacklist
        if extension not in self.extension_blacklist:
            # try to reload extension
            try:
                self.bot.unload_extension(self.extensions_dir + extension)
                self.bot.load_extension(self.extensions_dir + extension)
            except Exception as e:
                # create output embed
                embed = discord.Embed(
                    colour = discord.Colour.red(),
                    title = _("extension not reloaded, {extension}").format(extension=extension)
                )
                embed.add_field(name=_("Errors"), value="{}: {}".format(type(e).__name__, e), inline=False)

                # send embed
                await ctx.send(embed=embed)
            else:
                # create output embed
                embed = discord.Embed(
                    colour = discord.Colour.green(),
                    title = _("extension successfully reloaded, {extension}").format(extension=extension)
                )
                # send embed
                await ctx.send(embed=embed)
        else:
            # create output embed
            embed = discord.Embed(
                colour = discord.Colour.red(),
                title = _("extension not reloaded, {extension}").format(extension=extension)
            )
            embed.add_field(name=_("Errors"), value=_("extension blacklist"), inline=False)

            # send embed
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(ExtensionsManagement(bot))