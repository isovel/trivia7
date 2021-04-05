__authors__ = 'toastythetoaster'

import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
import pickledb

class trivia(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="test2")
    async def _test(self, ctx: SlashContext):
        embed = discord.Embed(title="embed test")
        await ctx.send(content="test", embeds=[embed])

def setup(bot):
    bot.add_cog(trivia(bot))
