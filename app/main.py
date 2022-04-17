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
        if self.user != message.author and self.profanity_filter.is_profane(message.content):
            logger.info(f'{message.author}: {message.content}')
            await message.channel.send(f'Watch your mouth, {message.author.mention}!')


if __name__ == '__main__':
    client = ProfanityBot()
    client.run(os.environ.get('DISCORD_TOKEN'))
