from discord import Client
from profanity_filter import ProfanityFilter
import logging
import os

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)


class ProfanityBot(Client):
    profanity_filter = ProfanityFilter()

    async def on_ready(self):
        logger.info(f'{self.user} is online!')

    async def on_message(self, message):
        if self.user == message.author:
            return
        
        logger.info(f'{message.author}: {message.content}')

        if self.profanity_filter.is_profane(message.content):
            await message.channel.send('Watch your mouth!')


if __name__ == '__main__':
    client = ProfanityBot()
    client.run(os.environ.get('DISCORD_TOKEN'))
