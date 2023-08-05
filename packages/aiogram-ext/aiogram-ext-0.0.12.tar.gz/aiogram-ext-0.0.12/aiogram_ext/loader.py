import logging

import mongoengine

from .bot import Bot
from .config import (
    BOT_TOKEN,
    MONGO_DB,
    MONGO_USER,
    MONGO_PASSWORD,
    MONGO_HOST,
)
from .deps import MongoStorage, Update
from .dispatcher import Dispatcher

bot = Bot(BOT_TOKEN)

storage = MongoStorage(
    db_name=MONGO_DB,
    host=MONGO_HOST,
    username=MONGO_USER,
    password=MONGO_PASSWORD,
)

dp = Dispatcher(bot, storage=storage)
logger = logging.getLogger()

mongoengine.connect(
    db=MONGO_DB,
    host=MONGO_HOST,
    username=MONGO_USER,
    password=MONGO_PASSWORD,
)


@dp.errors_handler()
async def _(update: Update, error: Exception):
    logger.exception(f"{error=} on {update=}")
    return True
