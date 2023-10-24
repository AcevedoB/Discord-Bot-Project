# ========================= IMPORT BLOCK ========================= #

#The following is a list of imports that are used in the cog. Please do not touch, this will be used in future rendentions of the DND  bot#

import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context

class General(commands.Cog, name='General Commands'):
  def __init__(self, bot):
    self.bot = bot
    
# ========== ADD COG TO THE BOT ========== #
async def setup(bot) -> None:
  await bot.add_cog(General(bot))
