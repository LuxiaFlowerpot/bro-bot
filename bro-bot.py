import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="bro-bot ")


@bot_event
async def on_ready():
    print('Connecté en tant que')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------------')
    await bot.change_presence(game=discord.Game(name="combattre Vega"))

bot.run(os.getenv('Token'))
