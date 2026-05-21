import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # BITNO za !komande

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot je online kao {bot.user}")

@bot.command()
async def test(ctx):
    await ctx.send("Hi tu sam")

@bot.tree.command(name="hello", description="Says hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello!")

@bot.event
async def setup_hook():
    await bot.tree.sync()

bot.run("TU_STAVI_TOKEN")
