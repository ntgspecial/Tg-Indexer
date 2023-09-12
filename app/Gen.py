from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = os.getenv('API_ID')
api_hash = os.getenv("API_HASH")

with TelegramClient(StringSession(), api_id, api_hash) as client:
    session_string = client.session.save()
    print(f"Your session string:\n{session_string}")
