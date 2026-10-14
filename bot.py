import asyncio
import os
import random

import discord
from discord.ext import commands

from bot_logic import gen_pass
from config import TOKEN


# A prof precisa disso pq não usa Windows ###########
if not discord.opus.is_loaded():
    for caminho_opus in [
        "/opt/homebrew/lib/libopus.dylib",
        "/usr/local/lib/libopus.dylib",
        "libopus.dylib",
    ]:
        try:
            discord.opus.load_opus(caminho_opus)
            break
        except Exception:  # noqa: BLE001, S110
            pass
#######################################################

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

@bot.command()
async def mentalista(ctx):

    text = "*Você mente pelo olhar... caso encerrado.*"

    with open('sounds/the_mentalist_edit.mp3', 'rb') as f:  # noqa: ASYNC230
        sound = discord.File(f)

    await ctx.send(text, file=sound)


@bot.command()
async def fahh(ctx):
    # Verificar se quem digitou o comando está em uma chamada de voz
    if not ctx.author.voice:
        await ctx.send("❌ Você precisa estar em um canal de voz!")
        return

    # Ver qual canal o autor da mensagem está
    canal = ctx.author.voice.channel

    # Conectar numa nova chamada ou continuar conectado (caso já esteja na correta)
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if not voice_client:
        voz = await canal.connect()
    elif voice_client.channel != canal:
        await voice_client.move_to(canal)
        voz = voice_client
    else:
        voz = voice_client

    # Se tiver tocando, para
    if voz.is_playing():
        voz.stop()

    # Pegar o caminho do som que vai tocar
    caminho_audio = "sounds/fahhhhh.mp3"

    # Tocar o som
    voz.play(discord.FFmpegPCMAudio(caminho_audio))

    # Espera terminar
    while voz.is_playing():
        await asyncio.sleep(1)

    # Desconectar do canal de voz
    await voz.disconnect()


@bot.command()
async def mentalista_voice(ctx):
    # Verificar se quem digitou o comando está em uma chamada de voz
    if not ctx.author.voice:
        await ctx.send("❌ Você precisa estar em um canal de voz!")
        return

    # Ver qual canal o autor da mensagem está
    canal = ctx.author.voice.channel

    # Conectar numa nova chamada ou continuar conectado (caso já esteja na correta)
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if not voice_client:
        voz = await canal.connect()
    elif voice_client.channel != canal:
        await voice_client.move_to(canal)
        voz = voice_client
    else:
        voz = voice_client

    # Se tiver tocando, para
    if voz.is_playing():
        voz.stop()

    # Pegar o caminho do som que vai tocar
    caminho_audio = "sounds/the_mentalist_edit.mp3"

    # Tocar o som
    voz.play(discord.FFmpegPCMAudio(caminho_audio))

    # Espera terminar
    while voz.is_playing():
        await asyncio.sleep(1)

    # Desconectar do canal de voz
    await voz.disconnect()


bot.run(TOKEN)