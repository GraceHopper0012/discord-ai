import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot
from discord import app_commands
import os

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="%", intents=intents)
tree = bot.tree

@bot.event
async def on_ready():
    synced = await bot.tree.sync(guild=None)
    print(f"Synced {len(synced)} commands")

@tree.command(name="talk", description="Let the AI respond")
@app_commands.describe(msg="The message to send to the AI")
async def talk(ctx, msg:str):
    ai_response = None # call Katja's function to talk to the AI here
    embed = discord.Embed(title="", description=ai_response)
    await ctx.response.send_message(embed=embed)

@tree.command(name="test", description="Test the bot")
async def test(ctx):
    embed = discord.Embed(title="Hello")
    await ctx.response.send_message(embed=embed)

# @tree.command(name="react", description="Let the AI react to the current conversation")


bot.run(os.getenv("DC_TOKEN"))
