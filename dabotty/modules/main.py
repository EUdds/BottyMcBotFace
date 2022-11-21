import os

from pathlib import Path
from dabotty.client import dabotty
from dotenv import load_dotenv



def main():
    here = Path(__file__).parent
    for module in here.glob('*.py'):
        if module.name == '__init__.py':
            continue
        if module.name == 'main.py':
            continue
        if module.name == 'template.py':
            continue
        dabotty.load_extension(f'dabotty.modules.{module.stem}')
    load_dotenv("tokens.env")
    dabotty.run(os.getenv('DISCORD_TOKEN'))



if __name__ == "__main__":
    main()