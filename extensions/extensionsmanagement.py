import discord
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
                    title = "\"" + extension + "\" was not loaded!"
                )
                embed.add_field(name="Errors", value="{}: {}".format(type(e).__name__, e), inline=False)

                # send embed
                await ctx.send(embed=embed)
            else:
                # create output embed
                embed = discord.Embed(
                    colour = discord.Colour.green(),
                    title = "\"" + extension + "\" was successfully loaded!"
                )
                # send embed
                await ctx.send(embed=embed)
        else:
            # create output embed
            embed = discord.Embed(
                colour = discord.Colour.red(),
                title = "\"" + extension + "\" was not loaded!"
            )
            embed.add_field(name="Errors", value="The extension is on the blacklist and may not be loaded/unloaded/reloaded", inline=False)

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
                    title = "\"" + extension + "\" was not unloaded!"
                )
                embed.add_field(name="Errors", value="{}: {}".format(type(e).__name__, e), inline=False)

                # send embed
                await ctx.send(embed=embed)
            else:
                # create output embed
                embed = discord.Embed(
                    colour = discord.Colour.green(),
                    title = "\"" + extension + "\" was successfully unloaded!"
                )
                # send embed
                await ctx.send(embed=embed)
        else:
            # create output embed
            embed = discord.Embed(
                colour = discord.Colour.red(),
                title = "\"" + extension + "\" was not loaded!"
            )
            embed.add_field(name="Errors", value="The extension is on the blacklist and may not be loaded/unloaded/reloaded", inline=False)

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
                    title = "\"" + extension + "\" was not reloaded!"
                )
                embed.add_field(name="Errors", value="{}: {}".format(type(e).__name__, e), inline=False)

                # send embed
                await ctx.send(embed=embed)
            else:
                # create output embed
                embed = discord.Embed(
                    colour = discord.Colour.green(),
                    title = "\"" + extension + "\" was successfully reloaded!"
                )
                # send embed
                await ctx.send(embed=embed)
        else:
            # create output embed
            embed = discord.Embed(
                colour = discord.Colour.red(),
                title = "\"" + extension + "\" was not loaded!"
            )
            embed.add_field(name="Errors", value="The extension is on the blacklist and may not be loaded/unloaded/reloaded", inline=False)

            # send embed
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(ExtensionsManagement(bot))