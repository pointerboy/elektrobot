import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='?', description='')

from requests import Session
from bs4 import BeautifulSoup as bs


@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)
    print('------')

with Session() as s:
    url= 'http://37.0.71.50/ets/login/index.php'
    site = s.get(url) 
    bs_content = bs(site.content, "html.parser")
    login_data = {"username":"luka.trbovic18", "password":"Ets!2345"}
    s.post(url, login_data)
    home_page = s.get('http://37.0.71.50/ets/course/view.php?id=285')
    print(home_page.content)

@bot.command()
async def saberi(ctx, left: float, right: float):
    await ctx.send(left + right)
    await ctx.send("Brzi od suzane (●'◡'●)(●'◡'●)")

bot.run('Njk0NTEyOTM3NTAyNjM4MTgw.XoMuVQ.j-VmuIqINxWz_gJaze-kL7wFREU')
