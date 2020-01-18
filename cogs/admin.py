import discord
from discord.ext import commands
from utilities import getConfig

class Admin(commands.Cog, name='Admin'):
    def __init__(self, bot):
        self.bot = bot
        self.config = getConfig()
        self.cogs_dir = 'cogs.'

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def load(self, ctx, module: str):
        try:
            self.bot.load_extension(self.cogs_dir + module)
        except Exception as e:
            await ctx.send(':x: "' + module + '" was not loaded. The following error message occurred:')
            await ctx.send('```{}: {}```'.format(type(e).__name__, e))
        else:
            await ctx.send(':white_check_mark: "' + module + '" was successfully loaded.')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unload(self, ctx, module : str):
        try:
            self.bot.unload_extension(self.cogs_dir + module)
        except Exception as e:
            await ctx.send(':x: "' + module + '" was not unloaded. The following error message occurred:')
            await ctx.send('```{}: {}```'.format(type(e).__name__, e))
        else:
            await ctx.send(':white_check_mark: "' + module + '" was successfully unloaded.')

    @commands.command(aliases=['r'])
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx, module : str):
        try:
            self.bot.unload_extension(self.cogs_dir + module)
            self.bot.load_extension(self.cogs_dir + module)
        except Exception as e:
            await ctx.send(':x: "' + module + '" was not reloaded. The following error message occurred:')
            await ctx.send('```{}: {}```'.format(type(e).__name__, e))
        else:
            await ctx.send(':white_check_mark: "' + module + '" was successfully reloaded.')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setplaceholders(self, ctx):
        await ctx.send(':clock10: An attempt is made to set all placeholder roles. This may take a few minutes.')
        try:
            if self.config['guild']['use_placeholders'] != "0":
                for guild in self.bot.guilds:
                    for member in guild.members:
                        tmpRoles = []
                        for role in member.roles:
                            tmpRoles.append(int(role.id))
                        for placeholder in self.config['guild']['use_placeholders'].split(','):
                            if int(placeholder) not in tmpRoles:
                                role = discord.utils.get(guild.roles, id=int(placeholder))
                                await member.add_roles(role)
        except Exception as e:
            await ctx.send(':x: Somthing went wrong. The following error message occurred:')
            await ctx.send('```{}: {}```'.format(type(e).__name__, e))
        else:
            await ctx.send(':white_check_mark: All placeholder roles was successfully set.')

def setup(bot):
    bot.add_cog(Admin(bot))