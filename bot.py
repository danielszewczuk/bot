import discord
from dotenv import load_dotenv
import os
from other import *
from ping3 import ping as ping3_ping
import datetime
import time

load_dotenv()
bot = discord.Bot()
@bot.event
async def on_ready():
    print(f"{bot.user} jest online!")
    await bot.change_presence(status=discord.Status.idle, activity = discord.Activity(type=discord.ActivityType.listening, name="/help"))

@bot.command(description="Wyświetla informacje o bocie.")
async def help(ctx):
    embed = discord.Embed(description="Wszystkie moje komendy znajdują się pod `/` \n Ten bot jest open source, jego kod możesz zobaczyć [tutaj](https://github.com/szewczuko/bot)", color=discord.Colour.brand_green())
    await ctx.respond(embed = embed)

@bot.command(name="8ball", description=" 🔮 Magiczna kula")
async def magiczna_kula(ctx, pytanie: discord.Option(str)):
    odpowiedz = losuj("other/8ball.txt")
    embed = discord.Embed(title=f"{odpowiedz}", color=discord.Colour.blurple())
    embed.set_author(name=f"{pytanie}", icon_url="https://em-content.zobj.net/source/microsoft/379/crystal-ball_1f52e.png")
    await ctx.respond(embed = embed)

@bot.command(name="say", description="Mówi coś z konta bota.")
async def say(ctx, wiadomosc: discord.Option(str)):
    await ctx.respond(wiadomosc)

# @bot.command(name="weekend", description="Sprawdza czas do weekendu.")
# async def weekend(ctx):
#     now = datetime.datetime.now()
#     if now.weekday() == 4 and now.hour >= 16 or now.weekday() == 5 or now.weekday() == 6 or (now.weekday() == 0 and now.hour < 16):
#         await ctx.respond("Jest weekend! <:tada:1193546704729944084> ")
#     else:
#         days_until_weekend = (4 - now.weekday() + 7) % 7
#         hours_until_weekend = 16 - now.hour
#         minutes_until_weekend = 0 - now.minute
#         time_until_weekend = datetime.timedelta(days=days_until_weekend, hours=hours_until_weekend, minutes=minutes_until_weekend)
#         weekend_start = now + time_until_weekend
#         weekend_start_timestamp = int(weekend_start.timestamp())
#         await ctx.respond(f"Do weekendu zostało: <t:{weekend_start_timestamp}:R>")

@bot.command(name="poezja", description="Randomowy cytat z kanału #cytaty.")
async def poezja(ctx):
    odpowiedz = losuj("other/cytaty.txt")
    await ctx.respond(odpowiedz)

@bot.command(name="isitup", description="Pinguje podany adres/domenę.")
async def isitup(ctx, adres):
    odpowiedz = isItUp(adres)
    if odpowiedz == True:
        await ctx.respond(f":white_check_mark: Adres `{adres}` jest online!")
    else:
        await ctx.respond(f":bangbang: Adres `{adres}` jest offline!")

bot.run(os.getenv('TOKEN'))