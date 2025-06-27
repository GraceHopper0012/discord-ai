import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot
from discord import app_commands
import os
import ai_back

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="%", intents=intents)
tree = bot.tree

talk_history = []

@bot.event
async def on_ready():
    synced = await bot.tree.sync(guild=None)
    print(f"Synced {len(synced)} commands")

@tree.command(name="talk", description="Let the AI respond")
@app_commands.describe(msg="The message to send to the AI")
async def talk(ctx, msg:str):
    # circumvent timeout
    await ctx.response.send_message("Wird generiert...")
    global talk_history
    talk_history.append({"role": "user", "content": msg})

    talk_history = talk_history[-10:]

    input_text = ""
    for message in talk_history:
        input_text += f"{message['role']}: {message['content']}\n"

    ai_response = ai_back.respond(input_text=input_text)

    talk_history.append({"role": "assistant", "content": ai_response})
    embed = discord.Embed(title="", description=ai_response)
    await ctx.edit_original_response(content=None, embed=embed)

@tree.command(name="test", description="Test the bot")
async def test(ctx):
    embed = discord.Embed(title="Hello")
    await ctx.response.send_message(embed=embed)

# @tree.command(name="react", description="Let the AI react to the current conversation")


bot.run(os.getenv("DC_TOKEN"))
