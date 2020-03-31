import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='?', description='')

from sajt import Sajt

@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    sajt = Sajt('luka.trbovic18', 'Ets!2345')

@bot.command()
async def saberi(ctx, left: float, right: float):
    await ctx.send(left + right)
    await ctx.send("Brzi od suzane (●'◡'●)(●'◡'●)")

bot.run('Njk0NTEyOTM3NTAyNjM4MTgw.XoMuVQ.j-VmuIqINxWz_gJaze-kL7wFREU')
