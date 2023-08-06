from asyncio import new_event_loop, sleep

import env
from aiohttp.web import Application, run_app

from viber.dispatcher.webhook import WebhookRequestHandler, BOT_DISPATCHER_KEY
from .bot import Bot
from .dispatcher import Dispatcher

BOT_TOKEN = env.get("BOT_TOKEN")
BOT_NAME = env.get("BOT_NAME")
APP_URL = env.get("APP_URL")
APP_PORT = env.get("APP_PORT", 80)
WEBHOOK_PATH = env.get("WEBHOOK_PATH", "/bot")


async def set_webhook():
    url = APP_URL + WEBHOOK_PATH
    await sleep(1)
    await bot.set_webhook(url)


bot = Bot(BOT_TOKEN, BOT_NAME)
dp = Dispatcher(bot)
app = Application()
app.router.add_post(WEBHOOK_PATH, WebhookRequestHandler)
app[BOT_DISPATCHER_KEY] = dp
loop = new_event_loop()


def run():
    loop.create_task(set_webhook())
    run_app(app, loop=loop, port=APP_PORT)
