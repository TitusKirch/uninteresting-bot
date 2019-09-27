import discord
from discord.ext import commands

class Admin(commands.Cog, name='Admin'):
    def __init__(self, bot):
        self.bot = bot
        self.cogs_dir = 'cogs.'

    @commands.command()
    async def load(self, ctx, module: str):
        try:
            self.bot.load_extension(self.cogs_dir + module)
        except Exception as e:
            await ctx.send(':x: "' + module + '" was not loaded. The following error message occurred:')
            await ctx.send('```{}: {}```'.format(type(e).__name__, e))
        else:
            await ctx.send(':white_check_mark: "' + module + '" was successfully loaded.')

    @commands.command()
    async def unload(self, ctx, module : str):
        try:
            self.bot.unload_extension(self.cogs_dir + module)
        except Exception as e:
            await ctx.send(':x: "' + module + '" was not unloaded. The following error message occurred:')
            await ctx.send('```{}: {}```'.format(type(e).__name__, e))
        else:
            await ctx.send(':white_check_mark: "' + module + '" was successfully unloaded.')

    @commands.command()
    async def reload(self, ctx, module : str):
        try:
            self.bot.unload_extension(self.cogs_dir + module)
            self.bot.load_extension(self.cogs_dir + module)
        except Exception as e:
            await ctx.send(':x: "' + module + '" was not reloaded. The following error message occurred:')
            await ctx.send('```{}: {}```'.format(type(e).__name__, e))
        else:
            await ctx.send(':white_check_mark: "' + module + '" was successfully reloaded.')

def setup(bot):
    bot.add_cog(Admin(bot))