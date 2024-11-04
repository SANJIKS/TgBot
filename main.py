import asyncio, logging, sys
from aiogram import Bot, Dispatcher
from app.handlers import router
from app.commands import set_commands
from decouple import config


TOKEN = config('TELEGRAM_TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(router)

async def main():
    await set_commands(bot)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot stopped')
