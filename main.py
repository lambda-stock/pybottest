from pyrogram import Client
from pyrogram import filters
import asyncio
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests
from requests import get
import os
import feedparser
import html
from bs4 import BeautifulSoup
from urllib.parse import urlsplit

#load_dotenv(".env", override=True)
bot_token = os.environ['BOT_TOKEN']
api_id = int(os.environ['API_ID'])
api_hash = os.environ['API_HASH']

app = Client(
    "lambdasession",
    api_id = api_id, api_hash = api_hash, bot_token = bot_token
)

NewsFeed = feedparser.parse("https://ww3turkce.xyz/haber/feed")

@app.on_message(filters.command("start"))
async def start(client, message):
    await client.send_message(message.chat.id, "Working.")
app.run()
