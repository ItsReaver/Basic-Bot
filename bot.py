import discord
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix="!")

token = "Your Token Here."

@client.event
async def on_ready():
    print("Bot Is Ready!")

@client.command()
async def hi(ctx):
    await ctx.send(f"Hi.")

@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

client.run(token)