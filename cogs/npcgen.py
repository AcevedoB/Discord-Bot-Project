# ========================= IMPORT BLOCK ========================= #
import os
import pandas
import random

import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context

# ========== NPCGEN CLASS ========== #


# ========== BROOKES CHILDREN ========== #
class NPCGen(commands.Cog, name='NPC Generation Commands'):

  def __init__(self, bot):
    self.bot = bot
    self.df = pandas.read_csv('DnD NPCs.csv')
  # Will generate a random npc name from the csv
  @commands.command()
  async def gen_npc_name(self, ctx):
    npc_name = random.choice(self.df['npc_name'])
    await ctx.send(npc_name)

  # Generates a random npc from the csv
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

    npc_level2 = int(npc_level)
    npc_age2 = int(npc_age)

    embed = discord.Embed(
        title="Generated NPC",
        url=
        "https://cdn.discordapp.com/attachments/1159242429954801737/1166083942273789972/getaloadofthisguy.png?ex=6549334c&is=6536be4c&hm=15b6ae3235b1e557cdce1af0&",
        description=f'```Name: {npc_name}```\
        ```Class: {npc_class}```\
        ```Race: {npc_race}```\
        ```Level: {npc_level2}```\
        ```Alignment: {npc_alignment}```\
        ```Gender: {npc_gender}```\
        ```Age: {npc_age2}```\
        ```Height: {npc_height}```\
        ```Description: {npc_description}```',
        color=0x004586)

    embed.set_author(name=ctx.author.display_name,
                     icon_url=ctx.author.avatar.url)

    await ctx.send(embed=embed)

  # Generates a random npc that is a level 5
  @commands.command()
  async def gen_npc_lvl(self, ctx):
    x = ctx.message.content.split()[1]
    matching_rows = []

    for index, row in self.df.iterrows():
      if row['npc_level'] == int(x):
        matching_rows.append(row)

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


# ========== ADD COG TO THE BOT ========== #
async def setup(bot) -> None:
  await bot.add_cog(NPCGen(bot))
