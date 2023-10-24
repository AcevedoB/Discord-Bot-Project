# ========================= IMPORT BLOCK ========================= #
import os
import pandas
import random

import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context

# ========== NPCGEN CLASS ========== #
class NPCGen(commands.Cog, name='NPC Generation Commands'):

  def __init__(self, bot):
    self.bot = bot
    self.df = pandas.read_csv('DnD NPCs.csv')

  # ========== GENERATES RANDOM NAME ========== #
  @commands.command()
  async def gen_random_name(self, ctx):
    npc_name = random.choice(self.df['npc_name'])

    # Embeds the npc in a pretty box :3
    embed = discord.Embed(
        title="Generated Name",
        url=
        "https://cdn.discordapp.com/attachments/1159242429954801737/1166083942273789972/getaloadofthisguy.png?ex=6549334c&is=6536be4c&hm=15b6ae3235b1e557cdce1af0&",
        description=f'{npc_name}',
        color=0x004586)

    embed.set_author(name=ctx.author.display_name,
                     icon_url=ctx.author.avatar.url)

    await ctx.send(embed=embed)

    # Deletes the message sent by the user
    await ctx.message.delete()

  # ========== GENERATES RANDOM NPC ========== #
  @commands.command()
  async def gen_npc(self, ctx):
    npc_name = random.choice(self.df['npc_name'])
    npc_class = random.choice(self.df['npc_class'])
    npc_race = random.choice(self.df['npc_race'])
    npc_level = random.choice(self.df['npc_level'])
    npc_alignment = random.choice(self.df['npc_alignment'])
    npc_gender = random.choice(self.df['npc_gender'])
    npc_age = random.choice(self.df['npc_age'])
    npc_height = random.choice(self.df['npc_height'])
    npc_description = random.choice(self.df['npc_description'])

    # Embeds the npc in a pretty box :3
    embed = discord.Embed(
        title="Generated NPC",
        url=
        "https://cdn.discordapp.com/attachments/1159242429954801737/1166083942273789972/getaloadofthisguy.png?ex=6549334c&is=6536be4c&hm=15b6ae3235b1e557cdce1af0&",
        description=f'```Name: {npc_name}```\
        ```Class: {npc_class}```\
        ```Race: {npc_race}```\
        ```Level: {int(npc_level)}```\
        ```Alignment: {npc_alignment}```\
        ```Gender: {npc_gender}```\
        ```Age: {int(npc_age)}```\
        ```Height: {npc_height}```\
        ```Description: {npc_description}```',
        color=0x004586)

    embed.set_author(name=ctx.author.display_name,
                     icon_url=ctx.author.avatar.url)

    await ctx.send(embed=embed)

    await ctx.message.delete()

  # ========== GENERATES RANDOM NPC WITH USER INPUT LVL ========== #
  @commands.command()
  async def gen_npc_lvl(self, ctx):
    x = ctx.message.content.split()[1]  # Splits the message into a 
    # list and takes the second index
    matching_rows = []

    # Fills the list with rows that match level inputed
    for index, row in self.df.iterrows():
      if row['npc_level'] == int(x):
        matching_rows.append(row)

    # Error messages for invalid inputs
    if not matching_rows:
      embed = discord.Embed(
          title="Error Message",
          url=
          "https://cdn.discordapp.com/attachments/1159242429954801737/1166083942273789972/getaloadofthisguy.png?ex=6549334c&is=6536be4c&hm=15b6ae3235b1e557cdce1af0&",
          description=f"'{x}' is not a valid level.",
          color=0xf90607)

      await ctx.send(embed=embed)
      return

    random_row = random.choice(matching_rows)
    npc_name = random_row['npc_name']
    npc_class = random_row['npc_class']
    npc_race = random_row['npc_race']
    npc_level = random_row['npc_level']
    npc_alignment = random_row['npc_alignment']
    npc_gender = random_row['npc_gender']
    npc_age = random_row['npc_age']
    npc_height = random_row['npc_height']
    npc_description = random_row['npc_description']

    embed = discord.Embed(
        title=f"NPC Level {x}",
        url=
        "https://cdn.discordapp.com/attachments/1159242429954801737/1166083942273789972/getaloadofthisguy.png?ex=6549334c&is=6536be4c&hm=15b6ae3235b1e557cdce1af0&",
        description=f'```Name: {npc_name}```\
        ```Class: {npc_class}```\
        ```Race: {npc_race}```\
        ```Level: {int(npc_level)}```\
        ```Alignment: {npc_alignment}```\
        ```Gender: {npc_gender}```\
        ```Age: {int(npc_age)}```\
        ```Height: {npc_height}```\
        ```Description: {npc_description}```',
        color=0x004586)

    embed.set_author(name=ctx.author.display_name,
                     icon_url=ctx.author.avatar.url)

    await ctx.send(embed=embed)

    # Deletes the message triggering the bot
    await ctx.message.delete()

  # ========== GENERATES RANDOM NPC WITH USER INPUT CLASS ========== #
  @commands.command()
  async def gen_npc_class(self, ctx):
    x = ctx.message.content.split()[1]  # Splits the message into a   list and takes the second index
    y = x.capitalize()
    matching_rows = []

    # Fills the list with rows that match level inputed
    for index, row in self.df.iterrows():
      if row['npc_class'] == (y):
        matching_rows.append(row)

    # Sends an error message if an invalid thing is inputted
    if not matching_rows:
      embed = discord.Embed(
          title="Error Message",
          url=
          "https://cdn.discordapp.com/attachments/1159242429954801737/1166083942273789972/getaloadofthisguy.png?ex=6549334c&is=6536be4c&hm=15b6ae3235b1e557cdce1af0&",
          description=f"'{y}' is not a valid class.",
          color=0xf90607)
          
      await ctx.send(embed=embed)
      return

    random_row = random.choice(matching_rows)
    npc_name = random_row['npc_name']
    npc_class = random_row['npc_class']
    npc_race = random_row['npc_race']
    npc_level = random_row['npc_level']
    npc_alignment = random_row['npc_alignment']
    npc_gender = random_row['npc_gender']
    npc_age = random_row['npc_age']
    npc_height = random_row['npc_height']
    npc_description = random_row['npc_description']

    embed = discord.Embed(
        title=f"NPC Class {y}",
        url=
        "https://cdn.discordapp.com/attachments/1159242429954801737/1166083942273789972/getaloadofthisguy.png?ex=6549334c&is=6536be4c&hm=15b6ae3235b1e557cdce1af0&",
        description=f'```Name: {npc_name}```\
        ```Class: {npc_class}```\
        ```Race: {npc_race}```\
        ```Level: {int(npc_level)}```\
        ```Alignment: {npc_alignment}```\
        ```Gender: {npc_gender}```\
        ```Age: {int(npc_age)}```\
        ```Height: {npc_height}```\
        ```Description: {npc_description}```',
        color=0x004586)

    embed.set_author(name=ctx.author.display_name,
                     icon_url=ctx.author.avatar.url)

    await ctx.send(embed=embed)

    await ctx.message.delete()

  # ========== USER INPUT LVL AND CLASS ========== #
  @commands.command()
  async def gen_npc_class_lvl(self, ctx):
    args = ctx.message.content.split()[1:]
    class_input = args[0]
    level_input = args[1]

    class_name = class_input.capitalize()
    level = int(level_input)
    
    matching_rows = []

    for index, row in self.df.iterrows():
      if row['npc_class'] == (class_name) and row['npc_level'] == (level):
        matching_rows.append(row)

    if not matching_rows:
      embed = discord.Embed(
          title="Error Message",
          url=
          "https://cdn.discordapp.com/attachments/1159242429954801737/1166083942273789972/getaloadofthisguy.png?ex=6549334c&is=6536be4c&hm=15b6ae3235b1e557cdce1af0&",
          description="This is not a valid input",
          color=0xf90607)

      await ctx.send(embed=embed)
      return

    random_row = random.choice(matching_rows)
    npc_name = random_row['npc_name']
    npc_class = random_row['npc_class']
    npc_race = random_row['npc_race']
    npc_level = random_row['npc_level']
    npc_alignment = random_row['npc_alignment']
    npc_gender = random_row['npc_gender']
    npc_age = random_row['npc_age']
    npc_height = random_row['npc_height']
    npc_description =        random_row['npc_description']

    embed = discord.Embed(
        title=f"Generated NPC",
        url=
        "https://cdn.discordapp.com/attachments/1159242429954801737/1166083942273789972/getaloadofthisguy.png?ex=6549334c&is=6536be4c&hm=15b6ae3235b1e557cdce1af0&",
        description=
      f'```Name: {npc_name}```\
        ```Class: {npc_class}```\
        ```Race: {npc_race}```\
        ```Level: {int(npc_level)}```\
        ```Alignment: {npc_alignment}```\
        ```Gender: {npc_gender}```\
        ```Age: {int(npc_age)}```\
        ```Height: {npc_height}```\
        ```Description: {npc_description}```',
        color=0x004586)

    embed.set_author(name=ctx.author.display_name,
                     icon_url=ctx.author.avatar.url)

    await ctx.send(embed=embed)

    await ctx.message.delete()
    

# ========== ADD COG TO THE BOT ========== #
async def setup(bot) -> None:
  await bot.add_cog(NPCGen(bot))
