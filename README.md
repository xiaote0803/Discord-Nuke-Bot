# Discord Nuke Bot

A powerful Discord server nuking bot

## Features

- Mass delete roles
- Mass delete channels
- Mass delete stickers
- Mass delete emojis
- Delete server templates
- Delete server icon
- Change server name
- Mass send messages (Webhook + Bot)
- Mass create channels
- Mass create colored roles

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

5. Use commands in bot DM:

```
!nuke server_id
```

## Important Notes

- Please ensure the bot has administrator permissions in the target server
- Use lowercase when setting channel names

## Disclaimer

This project is for educational and learning purposes only. I am not responsible for any damage caused by the use of this code. Users should use this tool responsibly and ensure compliance with all relevant terms of service and legal regulations.

