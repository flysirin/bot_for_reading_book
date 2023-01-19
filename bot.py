import asyncio
import logging

from aiogram import Bot, Dispatcher, executor
from config_data.config import Config, load_config
from handlers.other_handlers import register_echo_handler
from handlers.user_handlers import register_user_handlers
from keyboards.main_menu import set_main_menu

# init logger
logger = logging.getLogger(__name__)


# func for registration all handlers
def register_all_handlers(dp: Dispatcher) -> None:
    register_user_handlers(dp)
    register_echo_handler(dp)


# func for config and run Bot
async def main():
    # config logging
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s '
               u'[%(asctime)s] - %(name)s - %(message)s')

    # output in console info about start of the bot
    logger.info('Starting bot')

    # load the config into the config variable
    config: Config = load_config()

    # init the bot and the dispatcher
    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher(bot)

    # setting main menu of the bot
    await set_main_menu(dp)

    # register all handlers
    register_all_handlers(dp)

    # run polling
    try:
        await dp.start_polling()
    finally:
        await bot.close()


if __name__ == '__main__':
    try:
        # run func of main
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        # output in console error message
        # if get exception KeyboardInterrupt, SystemExit
        logger.error('Bot stopped!')
