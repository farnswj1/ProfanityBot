from discord import Client, Intents
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
        author = message.author
        content = message.content

        if self.user != author and self.profanity_filter.is_profane(content):
            logger.info(f'{author}: {content}')
            await message.channel.send(f'Watch your mouth, {author.mention}!')


if __name__ == '__main__':
    client = ProfanityBot(intents=Intents.default())
    client.run(os.environ.get('DISCORD_TOKEN'))
