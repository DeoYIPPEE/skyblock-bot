import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
DISCORD_TOKEN = str(os.getenv("DISCORD_TOKEN"))

bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("Skyblock bot is up!")
    try:
        synced = await bot.tree.sync()
        print("Skyblock bot synced!")
    except Exception as e:
        print(f"An exception occurred while syncing commands: {e}")

@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hey {interaction.user.mention}! This is a test command!", ephemeral=True)

@bot.tree.command(name="say")
@app_commands.describe(thing_to_say= "What should I say?")
async def say(interaction: discord.Interaction, thing_to_say: str):
    await interaction.response.send_message(f"{interaction.user.name} said `{thing_to_say}`")

@bot.tree.command(name="forge_flip", description="Gets the current most profitable forge flip")
async def forge_flip(interaction: discord.Interaction):
    embed = discord.Embed(title= "Title", description = f"Description\nDescription2")
    await interaction.response.send_message(embed=embed)

bot.run(DISCORD_TOKEN)