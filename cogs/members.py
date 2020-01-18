import discord
from discord.ext import commands
from utilities import getConfig
from utilities import getSpecialRoles

class Members(commands.Cog, name='Members'):
    def __init__(self, bot):
        self.bot = bot
        self.config = getConfig()
        self.specialRoles = getSpecialRoles()
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        if int(self.config['guild']['history_channel']) > 0:
            channel = member.guild.get_channel(int(self.config['guild']['history_channel']))
            if channel != None:
                await channel.send('**Welcome {0.mention} :tada:**'.format(member))
        if self.config['guild']['use_placeholders'] != "0":
            for placeholder in self.config['guild']['use_placeholders'].split(','):
                role = discord.utils.get(member.guild.roles, id=int(placeholder))
                await member.add_roles(role)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if int(self.config['guild']['history_channel']) > 0:
            channel = member.guild.get_channel(int(self.config['guild']['history_channel']))
            if channel != None:
                await channel.send('*Bye {0.mention} :sleepy:*'.format(member))

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        # check if roles change
        if before.roles != after.roles:

            # set member
            member = after
            guild = member.guild

            # get roles
            memberRoles = []
            for role in member.roles:
                memberRoles.append(int(role.id))
            
            # check if guest role isset
            if int(self.config['guild']['guest_role']) > 0:

                #check if rank roles are set
                if self.config['guild']['rank_roles'] != "0":

                    # setup
                    setGuest = True

                    # get ranks
                    ranks = []
                    for rank in self.config['guild']['rank_roles'].split(','):
                        ranks.append(int(rank))
                    
                    # add bot role to ranks
                    if int(self.config['guild']['bot_role']) > 0:
                        ranks.append(int(self.config['guild']['bot_role']))
                    
                    # check if member has one rank
                    for role in member.roles:
                        if int(role.id) in ranks:
                            setGuest = False
                            break
                    
                    # check if member get guest role
                    if setGuest:
                        # check if member has not guest role
                        if not int(self.config['guild']['guest_role']) in memberRoles:
                            # set guest role
                            role = discord.utils.get(guild.roles, id=int(self.config['guild']['guest_role']))
                            await member.add_roles(role)
                    else:
                        # check if member has guest role
                        if int(self.config['guild']['guest_role']) in memberRoles:
                            # remove guest role
                            role = discord.utils.get(guild.roles, id=int(self.config['guild']['guest_role']))
                            await member.remove_roles(role)

            # check if placeholder should be add or remove
            if self.config['guild']['use_placeholders'] != "0":
                isBot = False
                if int(self.config['guild']['bot_role']) > 0:
                    if int(self.config['guild']['bot_role']) in memberRoles:
                        isBot = True
                        for placeholder in self.config['guild']['use_placeholders'].split(','):
                            if int(placeholder) in memberRoles:
                                role = discord.utils.get(guild.roles, id=int(placeholder))
                                await member.remove_roles(role)
                
                if not isBot:
                    for placeholder in self.config['guild']['use_placeholders'].split(','):
                        if int(placeholder) not in memberRoles:
                            role = discord.utils.get(guild.roles, id=int(placeholder))
                            await member.add_roles(role)
            
            # check if gaming role isset
            if int(self.config['gaming']['general_role']) > 0:

                # check if member is in one gaming role
                hasGameRole = False
                for gameRole, gameRoleInfo in self.specialRoles['gaming'].items():
                    if int(gameRoleInfo['id']) in memberRoles:
                        hasGameRole = True
                        break
                    
                # check if member get general gaming role
                if hasGameRole:
                    # check if member has not general gaming role
                    if not int(self.config['gaming']['general_role']) in memberRoles:
                        # set general gaming role
                        role = discord.utils.get(guild.roles, id=int(self.config['gaming']['general_role']))
                        await member.add_roles(role)
                else:
                    # check if member has general gaming role
                    if int(self.config['gaming']['general_role']) in memberRoles:
                        # remove general gaming role
                        role = discord.utils.get(guild.roles, id=int(self.config['gaming']['general_role']))
                        await member.remove_roles(role)
            
                


def setup(bot):
    bot.add_cog(Members(bot))