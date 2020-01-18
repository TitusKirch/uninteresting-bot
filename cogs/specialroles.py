import discord
from discord.ext import commands
from utilities import getSpecialRoles

class SpecialRoles(commands.Cog, name='SpecialRoles'):
    def __init__(self, bot):
        self.bot = bot
        self.specialRoles = getSpecialRoles()
    
    @commands.command()
    async def roles(self, ctx):
        # setup
        result = ""
        result += str(ctx.author.mention) + "\nRoles can be joined/left with the command `!role roleName`. Alternatively the alias `!r` can be used and multiple roles (separated by spaces) can be specified. For example `!r roleA roleB roleC`\n"
        result += "You can join the following roles:\n\n"

        # foreach categories
        for category, roles in self.specialRoles.items():
            result += "**" + category.upper() + "**\n"
            result += "```"

            # foreach roles
            for command, role in roles.items():
                result += role['title'] + "\n"

            result += "```\n"

        await ctx.send(result)

    @commands.command(aliases=['r'])
    async def role(self, ctx, *args):

        # foreach filtered args
        for arg in list(filter(None, args)):

            # foreach categories
            for category, roles in self.specialRoles.items():

                # check if command exist
                if arg in roles:

                    # get and check role
                    role = roles[arg]
                    if role['id'] > 0:
                    
                        # set special role
                        specialRole = discord.utils.get(ctx.message.guild.roles, id=int(role['id']))

                        # check if member has role
                        if specialRole in ctx.author.roles:
                            await ctx.author.remove_roles(specialRole)
                            await ctx.message.channel.send(str(ctx.author.mention ) + " you leave the role \"" + role['title'] + "\"")
                        else:
                            await ctx.author.add_roles(specialRole)
                            await ctx.message.channel.send(str(ctx.author.mention ) + " you join the role \"" + role['title'] + "\"")
                        
                    # stop loop
                    break

def setup(bot):
    bot.add_cog(SpecialRoles(bot))