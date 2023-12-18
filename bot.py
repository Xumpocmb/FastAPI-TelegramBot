import uvicorn
from aiogram import Bot, Dispatcher, types
from fastapi import FastAPI

from tgbot.config import BOT_TOKEN, NGROK, DOMAIN, DEBUG
from tgbot.handlers import start_handler

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

app = FastAPI()
WEBHOOK_PATH = f"/bot/{BOT_TOKEN}"
if DEBUG == "dev":
    WEBHOOK_URL = f"{NGROK}{WEBHOOK_PATH}"
else:
    WEBHOOK_URL = f"{DOMAIN}{WEBHOOK_PATH}"


@app.on_event("startup")
async def on_startup():
    # Register routes
    dp.include_router(start_handler.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_webhook(WEBHOOK_URL)

    # webhook_info = await bot.get_webhook_info()
    # if webhook_info.url != WEBHOOK_URL:
    #     await bot.delete_webhook(drop_pending_updates=True)


@app.on_event("shutdown")
async def on_shutdown():
    await bot.session.close()


@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    await dp.feed_update(bot=bot, update=telegram_update)


if __name__ == "__main__":
    uvicorn.run(app, host="http://127.0.0.1", port=8000)
