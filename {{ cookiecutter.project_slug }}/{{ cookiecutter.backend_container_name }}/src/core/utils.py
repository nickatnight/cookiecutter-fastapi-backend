import platform

from r_dogecoin_bot.main import DogecoinMemeBot
from r_dogecoin_bot.types import RedditClientConfig

from src.core.config import settings
from src.db.clients.pg_client import PostgresSubmissionDbClient


platform_name = platform.uname()


async def botnet_run():
    reddit_config: RedditClientConfig = dict(
        client_id=settings.CLIENT_ID,
        client_secret=settings.CLIENT_SECRET,
        user_agent=f"{platform_name.release} {platform_name.machine} v3/{{ cookiecutter.project_slug }}",
    )
    bot = DogecoinMemeBot(
        reddit_client_config=reddit_config,
        db_client=PostgresSubmissionDbClient,
    )

    await bot.run()
