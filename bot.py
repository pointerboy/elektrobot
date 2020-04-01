import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='?', description='')

from sajt import Sajt

sajt = Sajt('luka.trbovic18', 'Ets!2345')

@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def saberi(ctx, left: float, right: float):
    await ctx.send(left + right)
    await ctx.send("Brzi od suzane (●'◡'●)(●'◡'●)")

@bot.command()
async def predmet_list(ctx, right):
    await ctx.send("Preuzimanje itema " + right)

    output = sajt.VratiItem(int(right))
    await ctx.send(output)
bot.run('Njk0NTEyOTM3NTAyNjM4MTgw.XoMuVQ.j-VmuIqINxWz_gJaze-kL7wFREU')
