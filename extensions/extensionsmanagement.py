import discord
from utilities import _
from discord.ext import commands
from models.extension import Extension
from db import db_session

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
                # load extension
                self.bot.load_extension(self.extensions_dir + extension)

                # check extension in database and update/set
                db_extension = Extension.get(extension)
                if db_extension:
                    db_extension.isLoaded = True
                else:
                    extension_object = Extension(extension, True)
                    db_session.add(extension_object)
                
                # commit update
                db_session.commit()


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
                # unload extension
                self.bot.unload_extension(self.extensions_dir + extension)

                # check extension in database and update/set
                db_extension = Extension.get(extension)
                if db_extension:
                    db_extension.isLoaded = False
                else:
                    extension_object = Extension(extension, False)
                    db_session.add(extension_object)
                
                # commit update
                db_session.commit()

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

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def extensions(self, ctx):

        # create output embeds
        embed_loaded = discord.Embed(
            colour = discord.Colour.green(),
            title = _("loaded extensions")
        )
        embed_unloaded = discord.Embed(
            colour = discord.Colour.red(),
            title = _("unloaded extensions")
        )

        # get loaded extension
        loaded_extensions = Extension.loaded()
        if loaded_extensions:
            for extension in loaded_extensions:
                embed_loaded.add_field(name=extension.name, value=extension.description, inline=False)
        else:
            embed_loaded.add_field(name=_("no extensions"), value=_("no extensions loaded"), inline=False)

        # get unloaded extension
        unloaded_extensions = Extension.unloaded()
        if unloaded_extensions:
            for extension in unloaded_extensions:
                embed_unloaded.add_field(name=extension.name, value=_(extension.description), inline=False)
        else:
            embed_unloaded.add_field(name=_("no extensions"), value=_("no extensions unloaded"), inline=False)

        # send embeds
        await ctx.send(embed=embed_loaded)
        await ctx.send(embed=embed_unloaded)

def setup(bot):
    bot.add_cog(ExtensionsManagement(bot))