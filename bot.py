import discord
import random
from discord.ext import commands

from bot_logic import gen_pass
from config import TOKEN
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='>', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def password(ctx, size=10):
    await ctx.send(gen_pass(size))

@bot.command()
async def meme(ctx):
    escolha = random.choice(os.listdir('memes'))
    with open(f'memes/{escolha}', 'rb') as f:  # noqa: ASYNC230
        image = discord.File(f)
    await ctx.send(file=image)

bot.run(TOKEN)