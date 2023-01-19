from aiogram import Dispatcher
from aiogram.types import Message


# This handler will respond to any text messages of the user
async def send_echo(message: Message):
    await message.answer(f'This is echo! {message.text}')


# func for handler registration
def register_echo_handler(dp: Dispatcher):
    dp.register_message_handler(send_echo)

