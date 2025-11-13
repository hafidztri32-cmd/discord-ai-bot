import os
import discord
from discord.ext import commands
import openai

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

openai.api_key = os.getenv("OPENAI_KEY")

@bot.event
async def on_ready():
    print(f"✅ Bot online sebagai {bot.user}")

@bot.command()
async def ai(ctx, *, prompt=None):
    if not prompt:
        await ctx.send("Ketik: `!ai [pertanyaan]`")
        return
    await ctx.send("⏳ Sedang berpikir...")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        reply = response["choices"][0]["message"]["content"]
        await ctx.send(reply)
    except Exception as e:
        await ctx.send(f"Terjadi kesalahan: {e}")

bot.run(os.getenv("DISCORD_TOKEN"))
