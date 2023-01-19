from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from lexicon.lexicon import LEXICON


# func generating a keyboard for a book page
def create_pagination_keyboard(*buttons: str) -> InlineKeyboardMarkup:
    # create object of keyboard
    pagination_kb: InlineKeyboardMarkup = InlineKeyboardMarkup()
    # set buttons to keyboards
    pagination_kb.row(*[InlineKeyboardButton(LEXICON[button] if button in LEXICON else button,
                                             callback_data=button) for button in buttons])
    return pagination_kb

