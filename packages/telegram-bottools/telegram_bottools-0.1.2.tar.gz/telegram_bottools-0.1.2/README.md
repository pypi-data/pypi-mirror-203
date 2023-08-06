# Create Telegram Bot
Telegram -> BotFather -> Type `/newbot`
https://core.telegram.org/bots/tutorial#creating-your-command

# Get Chat ID
https://api.telegram.org/bot<token>getUpdates

# Install
```
pip install telegram-bottools
```

# Config
```
bot_config = (chatid, token)
```

# Quick Start
```
from telegram_bottools import telegram_bottools as bot


bot_config = (-11111111, 'xxxxxx:yyyyyyyyyyy')
message = 'Hello World!'

bot.send_message(*bot_config, message)
```