import os

from dabotty.client.client import DaBottyClient
from dotenv import load_dotenv


def main():
    client = DaBottyClient()
    load_dotenv("tokens.env")
    client.run(os.getenv('DISCORD_TOKEN'))



if __name__ == "__main__":
    main()