import discord
import logging


class DaBottyClient(discord.Client):
    
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)
        self.logger = logging.getLogger('discord')
        self.logger.setLevel(logging.DEBUG)
        self.message_handlers = []

    
    async def on_ready(self):
        self.log('info', 'Logged in as %s' % self.user)

    async def on_message(self, message):
        for handler in self.message_handlers:
            await handler(message)
    
    def add_on_message_action(self, handler):
        print('debug', 'Added message handler %s' % handler)
        self.message_handlers.append(handler)
    
    def load_extension(self, extension):
        print('Loading extension %s' % extension)
        try:
            module_import = __import__(extension)
            extension_prefix = extension.split('.')[1]
            modules = getattr(module_import, extension_prefix)
            module = getattr(modules, extension.split('.')[2])
            if hasattr(module, 'register'):
                module.register()
            else:
                print('Extension %s does not have a register function' % extension)
        except Exception as e:
            print('Failed to load extension %s' % extension)
            raise e
    
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
        