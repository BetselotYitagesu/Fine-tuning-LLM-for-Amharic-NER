from telethon.sync import TelegramClient
import os
import pandas as pd

api_id = 24761492
api_hash = '253488c98e49fc4b4d191d8955f52891'
phone = '+251911903010'

channels = [
    'https://t.me/@ethio_brand_collection',
    'https://t.me/Leyueqa',
    'https://t.me/marakibrand',
    'https://t.me/qnashcom',
    'https://t.me/MerttEka',
]

output_dir = 'data/raw'
os.makedirs(output_dir, exist_ok=True)

with TelegramClient('ethioner', api_id, api_hash) as client:
    for url in channels:
        channel_name = url.split('/')[-1]
        print(f"Fetching from: {channel_name}")
        messages = []
        for message in client.iter_messages(channel_name, limit=200):
            if message.message:
                messages.append({
                    'channel': channel_name,
                    'date': message.date,
                    'message': message.message,
                    'views': message.views,
                    'id': message.id
                })
        df = pd.DataFrame(messages)
        df.to_csv(f"{output_dir}/{channel_name}.csv", index=False)
