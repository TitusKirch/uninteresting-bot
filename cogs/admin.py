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
        if self.config['guild']['use_placeholders'] != "0":
            await ctx.send(':clock10: An attempt is made to set all placeholder roles. This may take a few minutes.')
            try:
                for guild in self.bot.guilds:
                    for member in guild.members:
                        tmpRoles = []
                        for role in member.roles:
                            tmpRoles.append(int(role.id))

                        if int(self.config['guild']['bot_role']) > 0:
                            if int(self.config['guild']['bot_role']) in tmpRoles:
                                for placeholder in self.config['guild']['use_placeholders'].split(','):
                                    if int(placeholder) in tmpRoles:
                                        role = discord.utils.get(guild.roles, id=int(placeholder))
                                        await member.remove_roles(role)
                                continue

                        for placeholder in self.config['guild']['use_placeholders'].split(','):
                            if int(placeholder) not in tmpRoles:
                                role = discord.utils.get(guild.roles, id=int(placeholder))
                                await member.add_roles(role)
            except Exception as e:
                await ctx.send(':x: Somthing went wrong. The following error message occurred:')
                await ctx.send('```{}: {}```'.format(type(e).__name__, e))
            else:
                await ctx.send(':white_check_mark: All placeholder roles was successfully set.')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setguests(self, ctx):
        if int(self.config['guild']['guest_role']) > 0:
            await ctx.send(':clock10: An attempt is made to set all guest roles. This may take a few minutes.')
            try:
                for guild in self.bot.guilds:
                    for member in guild.members:
                        setGuest = True

                        placeholders = [] 
                        if self.config['guild']['use_placeholders'] != "0":
                            tmpPlaceholders = self.config['guild']['use_placeholders'].split(',')
                            for placeholder in tmpPlaceholders:
                                placeholders.append(int(placeholder))
                        
                        tmpRoles = []
                        for role in member.roles:
                            tmpRoles.append(int(role.id))
                            if int(role.id) == int(self.config['guild']['guest_role']):
                                continue
                            elif int(role.id) in placeholders:
                                continue
                            elif int(self.config['guild']['rule_message']) > 0 and int(self.config['guild']['rule_role']) > 0 and int(self.config['guild']['rule_role']) == int(role.id):
                                continue
                            elif str(role) == "@everyone":
                                continue
                            else:
                                setGuest = False
                                break
                        
                        if setGuest:
                            if not int(self.config['guild']['guest_role']) in tmpRoles:
                                role = discord.utils.get(guild.roles, id=int(self.config['guild']['guest_role']))
                                await member.add_roles(role)
                        else:
                            if int(self.config['guild']['guest_role']) in tmpRoles:
                                role = discord.utils.get(guild.roles, id=int(self.config['guild']['guest_role']))
                                await member.remove_roles(role)

            except Exception as e:
                await ctx.send(':x: Somthing went wrong. The following error message occurred:')
                await ctx.send('```{}: {}```'.format(type(e).__name__, e))
            else:
                await ctx.send(':white_check_mark: All guest roles was successfully set.')

def setup(bot):
    bot.add_cog(Admin(bot))