from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from lexicon.lexicon import LEXICON
from services.file_handling import book


def create_bookmarks_keyboard(*args: int) -> InlineKeyboardMarkup:
    # create obj keyboard
    bookmarks_kb: InlineKeyboardMarkup = InlineKeyboardMarkup()
    # set keyboard buttons-bookmarks
    for button in sorted(args):
        bookmarks_kb.add(InlineKeyboardButton(
            text=LEXICON['edit_bookmarks_button'],
            callback_data='edit_bookmarks'),
            InlineKeyboardButton(text=LEXICON['cancel'],
                                 callback_data='cancel'))
    return bookmarks_kb


def create_edit_keyboard(*args: int) -> InlineKeyboardMarkup:
    # create obj of keyboard
    bookmarks_kb: InlineKeyboardMarkup = InlineKeyboardMarkup()
    # set keyboard buttons-bookmarks
    for button in sorted(args):
        bookmarks_kb.add(InlineKeyboardButton(
            text=f'{LEXICON["del"]} {button} - {book[button][:100]}',
            callback_data=f'{button}del'))
    # add button "Отменить" to end of keyboard
    bookmarks_kb.add(InlineKeyboardButton(
        text=LEXICON['cancel'],
        callback_data='cancel'))
    return bookmarks_kb

