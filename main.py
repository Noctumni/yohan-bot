import discord
from discord.ext import commands
import random
import json
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='owo ', intents=intents)

# Load or create user data
def load_data():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except:
        return {}

def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

user_data = load_data()

def get_balance(user_id):
    return user_data.get(str(user_id), {}).get("cowoncy", 0)

def add_balance(user_id, amount):
    uid = str(user_id)
    if uid not in user_data:
        user_data[uid] = {"cowoncy": 0, "inventory": []}
    user_data[uid]["cowoncy"] += amount
    save_data(user_data)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def balance(ctx):
    bal = get_balance(ctx.author.id)
    await ctx.send(f'{ctx.author.name}, you have 💴 {bal} cowoncy!')

@bot.command()
async def hunt(ctx):
    reward = random.randint(10, 50)
    add_balance(ctx.author.id, reward)
    await ctx.send(f'🎯 You went hunting and earned 💴 {reward} cowoncy!')

@bot.command()
async def owoify(ctx, *, text):
    owo_text = text.replace('r', 'w').replace('l', 'w').replace('R', 'W').replace('L', 'W')
    await ctx.send(f'{owo_text} uwu')

bot.run(os.environ['DISCORD_TOKEN'])
