import discord
import logging


class DaBottyClient():
    client: discord.Client = discord.Client(intents=discord.Intents.default())
    
    def __init__(self):
        self.logger = logging.getLogger('discord')

    
    async def on_ready(self):
        print(f'{self.client.user} has connected to Discord!')
    

    def add_event(self, event, kwargs):
        self.client.event(event)
    
    def run(self, token):
        self.log('info', 'Starting DaBotty')
        self.client.event(self.on_ready)
        self.client.run(token)
    
    def log(self, level, message):
        if level == 'info':
            self.logger.info(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        elif level == 'critical':
            self.logger.critical(message)
        elif level == 'debug':
            self.logger.debug(message)
        else:
            self.logger.info(message)
        