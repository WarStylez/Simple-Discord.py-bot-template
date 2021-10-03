import discord
import json
from discord.ext import commands

with open("./data/config.json", "r") as configjsonFile:
    configData = json.load(configjsonFile)
    TOKEN = configData["token"]
    PREFIX = configData["prefix"]


intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, description="My first bot!", activity=discord.Game(name="Do !help"), intents=intents) # if you have a custom help command add help_command=None

@bot.event
async def on_command_error(ctx, error):
    pass

@bot.event
async def on_ready():
    print("Loaded")
    
@bot.command()
async def ping(ctx):
    await ctx.send(value=str(f"My ping is: {round(bot.latency * 10)}ms")

bot.run(token)
