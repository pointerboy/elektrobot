import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='?', description='')

from sajt import Sajt

import os 

sajt = Sajt('luka.trbovic18', 'Ets!2345')

@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def saberi(ctx, left: float, right: float):
    await ctx.send(left + right)

@bot.command()
async def predmet_list(ctx, right):
    await ctx.send("Preuzimanje itema " + right)

    output = sajt.VratiItem(int(right))
    await ctx.send(output)
bot.run(os.getenv('KEY'))
