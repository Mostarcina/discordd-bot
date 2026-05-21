import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot je online kao {bot.user}")

@bot.command()
async def test(ctx):
    await ctx.send("Hi tu sam")

bot.run("MTUwNzEwODM5MjQwODQ0OTAzNA.GEAUDV.KdHvBcQ1vAx__-BRkuq_i7mJi-9PHLTFJ1DiRI")
