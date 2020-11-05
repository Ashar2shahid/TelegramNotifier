from telethon.sync import TelegramClient, events
from dotenv import load_dotenv
import re
import os

load_dotenv(override=True)

api_id = os.getenv("API_ID") #Personal API
api_hash = os.getenv("API_HASH") #Personal API
phone = os.getenv("PHONE") #Phone Number used for Personal API
username = os.getenv("USERNAME") #Personal Username
bot_token = os.getenv("BOT_TOKEN") #Bot API token

GROUP_ENTITY_ID = -1001196383496 #Delhi Visa slots ID

with TelegramClient(username, api_id, api_hash).start(phone=phone) as client:
    with TelegramClient('bot',api_id,api_hash).start(bot_token=bot_token) as bot:

        @bot.on(events.NewMessage()) #On Subscribe to Bot / On MessageBot
        async def handler(event):
            sender = await event.get_sender()
            print(sender.username)
            print(sender.id)
            await event.reply("Hi, I am bot")            

        @client.on(events.NewMessage(GROUP_ENTITY)) #On Message from Group
        async def handler(event):
            if re.search(r'\bGO\b',event.raw_text,re.IGNORECASE): # if text contains GO message
                usernames = [user.id for user in await client.get_participants(GROUP_ENTITY_ID)] # GET ALL PARTICIPANTS OF GROUP
                for users in usernames:
                    try:
                        await bot.send_message(users, 'CHECK SLOTS RIGHT NOW')
                    except Exception as e:
                        continue

            

        client.run_until_disconnected()