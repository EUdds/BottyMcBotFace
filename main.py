import os
import discord
import logging

from dotenv import load_dotenv

logging.basicConfig()


intents = discord.Intents.default()
# intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')



def main():
    load_dotenv("tokens.env")
    client.run(os.getenv("DISCORD_TOKEN"))

if __name__ == '__main__':
    main()