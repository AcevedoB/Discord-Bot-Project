# ========================= IMPORT BLOCK ========================= #
# You can ensure all the correct modules are installed by running:
# pip install -r requirements.txt
# in the Repl.it Shell.

import keep_alive
import os
import random

import discord
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks

# ========== ENVIRONMENTAL VARIABLES ========== #
TOKEN = os.environ['DISCORD_TOKEN']
GUILD = os.environ['DISCORD_GUILD']


# ========== NPCFORGE CLASS ========== #
class NPCForge(commands.Bot):

  def __init__(self, command_prefix, intents):
    super().__init__(command_prefix=command_prefix, intents=intents)

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
    # Ensures the bot is ready before starting the status changing task
    await self.wait_until_ready()

  async def on_connect(self):
    self.status_task.start()
    # you can add other lines of code here to run when the bot starts!

  # hey team! create more commands here!
  # make sure you're indenting so everything falls under the NPCForge class. thanks! <3


# ========== CREATING INSTANCE OF INTENTS ========== #
intents = discord.Intents.all()
intents.messages = True

# ========== INITIALIZING NPCFORGE ========== #
client = NPCForge(command_prefix='!', intents=intents)
keep_alive.keep_alive()  # Keeps the bot up and running!
client.run(TOKEN)
