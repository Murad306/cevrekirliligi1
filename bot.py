import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="$komutlar")) 
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command('genc_kitle')
async def genc_kitle(ctx):
    await ctx.send(f'Merhaba genc hedef kitlesi icin ilk once evde suyu kullananlar icin evde suyu az kullanmalari icin onlara suyu zamaninda kapatmalari icin hatirlatma yapmalari gerek ve pet sise kullanimini minimuma indirmeleri gerek')

@bot.command('su_kullanimi')
async def genc_kitle(ctx):
    await ctx.send(f'https://www.youtube.com/watch?v=FLp8HWhuVyw&pp=ygUec3UgdGFzYXJydWZ1IGlsZ2lsaXNpIHZpZGVvbGFy - videonun linkini arata bilirsin')

@bot.command('komutlar')
async def komutlar(ctx):
    await ctx.send(f'genc_kitle / su_kullanimi / (yeni komutlar yakinda)')
bot.run("MTI5MjU0MTIyOTQ3MjQxNTc0NA.GP1kSV.6wdE5lHAjH9E1KqtraMWZ9aAsHKm4Q2QdF3faY")