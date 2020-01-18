import discord
from discord.ext import commands
from utilities import getConfig

class Members(commands.Cog, name='Members'):
    def __init__(self, bot):
        self.bot = bot
        self.config = getConfig()
    
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
            
            # check if guest should be add or remove
            if int(self.config['guild']['guest_role']) > 0:
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
                        role = discord.utils.get(member.guild.roles, id=int(self.config['guild']['guest_role']))
                        await member.add_roles(role)
                else:
                    if int(self.config['guild']['guest_role']) in tmpRoles:
                        role = discord.utils.get(member.guild.roles, id=int(self.config['guild']['guest_role']))
                        await member.remove_roles(role)

def setup(bot):
    bot.add_cog(Members(bot))