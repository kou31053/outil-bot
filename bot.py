import os
from threading import Thread
import discord
from discord.ext import commands
from flask import Flask

# --- Web Server giữ bot online ---
app = Flask('')


@app.route('/')
def home():
  return 'Bot is running!'


def run_web():
  # Render sẽ cấp một cổng PORT tự động
  port = int(os.environ.get('PORT', 8080))
  app.run(host='0.0.0.0', port=port)


def keep_alive():
  t = Thread(target=run_web)
  t.start()


# --- Code Discord Bot của bạn ---
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

MY_DISCORD_ID = 1455830724744712327  # Thay bằng ID của bạn


@bot.event
async def on_ready():
  print(f'Bot {bot.user} đã sẵn sàng 24/7!')


@bot.command()
async def noi(ctx, *, noidung: str):
  if ctx.author.id != MY_DISCORD_ID:
    return
  await ctx.message.delete()
  await ctx.send(noidung)


# Chạy web server trước, sau đó chạy bot
keep_alive()
TOKEN = os.environ.get("DISCORD_TOKEN", "MTU2OTM4NjEyNzI5NzYxMzk1NQ.G20S3N.fWmaIvcz9bBIvluglLcmLz_VkeRvsCPtJ8IYcw")
bot.run(TOKEN)