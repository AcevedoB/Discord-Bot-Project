# ========================= IMPORT BLOCK ========================= #
# You can ensure all the correct modules are installed by running:
# pip install -r requirements.txt
# in the Repl.it Shell.

import json
import os
import random
import sys

import discord
import discord.ext
from discord.ext import commands, tasks

import keep_alive

# ========== LOAD CONFIG FILE ========== #
if not os.path.isfile(
    f'{os.path.realpath(os.path.dirname(__file__))}/config.json'):
  sys.exit('config.json not found!')
else:
  with open(
      f'{os.path.realpath(os.path.dirname(__file__))}/config.json') as file:
    config = json.load(file)

# ========== ENVIRONMENTAL VARIABLES ========== #
TOKEN = os.environ['DISCORD_TOKEN']
GUILD = os.environ['DISCORD_GUILD']

# These variables have been defined in the repl.


# ========== NPCFORGE CLASS ========== #
class NPCForge(commands.Bot):

  def __init__(self) -> None:
    super().__init__(command_prefix=commands.when_mentioned_or(config['prefix']), intents=intents)
    # Creates custom bot variables so they can be accessed in cog files.
    self.config = config

  # ========== LOAD COGS ========== #
  async def load_cogs(self) -> None:
    # Iterates over each file in the "cogs" folder.
    for file in os.listdir(
        f"{os.path.realpath(os.path.dirname(__file__))}/cogs"):
      # Checks if the file is a .py file.
      if file.endswith(".py"):
        # Removes the .py extension using slice notation [:-3].
        # Only the file name is stored in the extension.
        extension = file[:-3]
        try:
          # Attempts to load extensions from "cogs".
          await self.load_extension(f"cogs.{extension}")
          print(f'Loaded extension \'{extension}\'')
        except Exception as e:
          # Throws an error if the extension fails to load.
          exception = f"{type(e).__name__}: {e}"
          print(f"Failed to load extension \'{extension}\'\n{exception}")

  async def on_ready(self):
    guild = discord.utils.get(self.guilds, name=GUILD)
    # Prints name and ID of connected guild(s) when the bot is ready.
    print(f'{self.user.name} is connected to the following guild:\n'
          f'{guild.name}(id: {guild.id})')

  @tasks.loop(minutes=1.0)
  async def status_task(self) -> None:
    # Sets up the game status for NPCForge. (Background task keeps the bot running)
    statuses = [
        'Serenading the crowd at the Dragon\'s Tavern!',
        'Mixing up special drinks at the Dragon\'s Tavern...',
        'Documenting epic tales of the Tavern\'s newest heroes...',
        'Playing pranks in the Dragon\'s Tavern!',
        'Organizing a dragon-slaying crew at the Dragon\'s Tavern...',
        'Discussing the latest unearthed arcana at the Dragon\'s Tavern!',
    ]
    await self.change_presence(activity=discord.Game(random.choice(statuses)))

  @status_task.before_loop
  async def before_status_task(self) -> None:
    # Ensures the bot is ready before starting status changing task
    await self.wait_until_ready()

  async def on_connect(self):
    await self.load_cogs()
    self.status_task.start()


# ========== CREATING INSTANCE OF INTENTS ========== #
intents = discord.Intents.all()
intents.messages = True

# ========== INITIALIZING NPCFORGE ========== #
client = NPCForge()


#This is my testing ground for "The Box"
@client.command()
async def embed(ctx):
  embed = discord.Embed(
      title="Embed",
      url="",
      description=
      "This took way to long, and is my only contributuion to this assignemtn and it was all for nothing. Now, I will lay down in a hole and wait for the sweet delevery of death to take its hold over me and take the essence of life from my lungs and veins.",
      color=0x004586)

  embed.set_author(name=ctx.author.display_name)

  await ctx.send(embed=embed)


keep_alive.keep_alive()  # Keeps the bot up and running!
client.run(TOKEN)
