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
        result = "You can join the following roles:\n"
        result += "*(Each group name is preceded by the required command to join. This **always** starts with a ?)*\n\n\n"

        # foreach categories
        for category, roles in self.specialRoles.items():
            result += "**" + category.upper() + "**\n"
            result += "```"

            # foreach roles
            for command, role in roles.items():
                result += "?" + command + " => " + role['title'] + "\n"

            result += "```\n\n"

        
        await ctx.send(result)
    
    @commands.Cog.listener()
    async def on_message(self, message):

        # check if message start with ?
        if message.content.startswith('?'):

            # foreach categories
            for category, roles in self.specialRoles.items():

                # check if command exist
                if message.content.split('?')[1] in roles:
                    
                    # get and check role
                    role = roles[message.content.split('?')[1]]
                    if role['id'] > 0:
                    
                        # set special role
                        specialRole = discord.utils.get(message.guild.roles, id=int(role['id']))

                        # check if member has role
                        if specialRole in message.author.roles:
                            await message.author.remove_roles(specialRole)
                            await message.channel.send(str(message.author.mention ) + " you leave the role \"" + role['title'] + "\"")
                        else:
                            await message.author.add_roles(specialRole)
                            await message.channel.send(str(message.author.mention ) + " you join the role \"" + role['title'] + "\"")
                        
                    # stop loop
                    break


def setup(bot):
    bot.add_cog(SpecialRoles(bot))