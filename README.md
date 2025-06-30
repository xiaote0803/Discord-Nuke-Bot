# Discord Nuke Bot

A powerful Discord nuke bot

## Features

- Ban other bots
- Mass delete roles
- Mass delete channels
- Mass delete stickers
- Mass delete emojis
- Delete server templates
- Delete server icon
- Change server name
- Mass send messages (Webhook + Bot)
- Mass create channels
- Mass create roles

## Usage

1. Clone this repository to your local machine
2. Install required packages:

```bash
pip install requirements.txt
```

3. Configure the following variables in the `bot.py` file:

```python
channel_name = "CHANNEL_NAME"
role_name = "ROLE_NAME"
server_name = "SERVER_NAME"
webhook_name = "WEBHOOK_NAME"
message = "MESSAGE_CONTENT"
token = "YOUR_BOT_TOKEN"
```

4. Run the bot:

```bash
python3 bot.py
```

5. Use command in bot DM:

```
!nuke server_id
```

## Notes

- Please check the bot has admin permissions in the target server
- Move the bot's role as high as possible in the role list
- Use lowercase when setting channel names

## Disclaimer

This project is for educational purposes only. Use at your own risk. Users are responsible for complying with all applicable laws and terms of service.

