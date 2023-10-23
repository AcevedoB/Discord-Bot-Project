# ========================= IMPORT BLOCK ========================= #
import pandas
import random

import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context


# ========== VICIOUS MOCKERY CLASS ========== #
class ViciousMockery(commands.Cog, name='Vicious Mockery Quotes'):

  def __init__(self, bot):
    self.bot = bot
    self.mockery = pandas.read_csv('Vicious_Mockery.csv')
    self.shakespeare = pandas.read_csv('Shakespeare.csv')

  # ========== VICIOUS MOCKERY ========== #
  @commands.command()
  async def mock(self, ctx, *, username: discord.Member = None):
    # Check if username is provided:
    if username is not None:
      # Embed text
      embed = discord.Embed(
          description=
          f"{random.choice(self.mockery['quote'])}, {username.mention}")
      # Embed author
      embed.set_author(name=ctx.author.display_name,
                       icon_url=ctx.author.avatar.url)
      # Sends embed
      await ctx.send(embed=embed)
    # If username is not provided:
    else:
      # Embed text
      embed = discord.Embed(description=random.choice(self.mockery['quote']))
      # Embed author
      embed.set_author(name=ctx.author.display_name,
                       icon_url=ctx.author.avatar.url)
      # Sends embed
      await ctx.send(embed=embed)

  # ========== SHAKESPEARE ========== #
  @commands.command()
  async def shake(self, ctx, *, username: discord.Member = None):
    # Check if username is provided:
    if username is not None:
      # Embed text
      embed = discord.Embed(
          description=
          f"{random.choice(self.shakespeare['quote'])}, {username.mention}")
      # Embed author
      embed.set_author(name=ctx.author.display_name,
                       icon_url=ctx.author.avatar.url)
      # Sends embed
      await ctx.send(embed=embed)
    # If username is not provided:
    else:
      # Embed text
      embed = discord.Embed(
          description=random.choice(self.shakespeare['quote']))
      # Embed author
      embed.set_author(name=ctx.author.display_name,
                       icon_url=ctx.author.avatar.url)
      # Sends embed
      await ctx.send(embed=embed)

  # ========== PAIN AND SUFFERING ========== #
  @commands.command()
  async def pain(self, ctx, *, username: discord.Member = None):
    pain = [
        "Kill yourself", "Your life means nothing", "Blow your brains out",
        "You're a failure", "Do better", "Worthless sack of shit",
        "*Smacks your head with a weighted stuffie*",
        "Shut the fuck up, you sound stupid",
        "At least I have a family that loves me", "Lmao are you crying?",
        "Quit being a Mia"
    ]

    if username is not None:
      await ctx.send(f"{random.choice(pain)}, {username.mention}")
    else:
      await ctx.send(random.choice(pain))

  # ========== GET A LOAD OF THIS GUY ========== #
  @commands.command()
  async def cope(self, ctx, *, username: discord.Member = None):
    # Check if username is provided:
    if username is not None:
      # Embed text
      embed = discord.Embed(
          description=
          f"Lmao get a loada this guy \n:point_right: {username.mention}")
      # Embed author
      embed.set_author(name=ctx.author.display_name,
                       icon_url=ctx.author.avatar.url)
      # Embed thumbnail
      embed.set_thumbnail(
          url=
          "https://cdn.discordapp.com/attachments/1159242429954801737/1166083942273789972/getaloadofthisguy.png?ex=6549334c&is=6536be4c&hm=15b6ae3235b1e557cdce1af0&"
      )
      # Sends embed
      await ctx.send(embed=embed)
    # If username is not provided:
    else:
      # Embed text
      embed = discord.Embed(description=f"Lmao get a loada this guy")
      # Embed author
      embed.set_author(name=ctx.author.display_name,
                       icon_url=ctx.author.avatar.url)
      # Embed thumbnail
      embed.set_thumbnail(
          url=
          "https://cdn.discordapp.com/attachments/1159242429954801737/1166083942273789972/getaloadofthisguy.png?ex=6549334c&is=6536be4c&hm=15b6ae3235b1e557cdce1af0&"
      )
      # Sends embed
      await ctx.send(embed=embed)


# ========== ADD COG TO THE BOT ========== #
async def setup(bot) -> None:
  await bot.add_cog(ViciousMockery(bot))
