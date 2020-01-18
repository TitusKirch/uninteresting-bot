import discord
from discord.ext import commands
from utilities import getConfig

class Rules(commands.Cog, name='Rules'):
    def __init__(self, bot):
        self.bot = bot
        self.config = getConfig()

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if int(self.config['guild']['rule_message']) > 0:
            if int(self.config['guild']['rule_role']) > 0:
                if payload.message_id == int(self.config['guild']['rule_message']):
                    if str(payload.emoji.name) == '✅':
                        guild = self.bot.get_guild(payload.guild_id)
                        member = guild.get_member(payload.user_id)
                        role = discord.utils.get(guild.roles, id=int(self.config['guild']['rule_role']))
                        await member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if int(self.config['guild']['rule_message']) > 0:
            if int(self.config['guild']['rule_role']) > 0:
                if payload.message_id == int(self.config['guild']['rule_message']):
                    if str(payload.emoji.name) == '✅':
                        guild = self.bot.get_guild(payload.guild_id)
                        member = guild.get_member(payload.user_id)
                        role = discord.utils.get(guild.roles, id=int(self.config['guild']['rule_role']))
                        await member.remove_roles(role)

def setup(bot):
    bot.add_cog(Rules(bot))