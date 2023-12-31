from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from lexicon.lexicon import LEXICON


# Функция, возвращаю builder с клавиатурой для bookmarks
def create_bookmarks_buttons(indi, bm_list):
    # Создаем builder и пустой list для добавления в него кнопок
    bookmarks_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    bm_buttons: list[InlineKeyboardButton] = []

    # Добавляем все кнопки в один list для добавления через row
    for i in sorted(bm_list):
        bm_buttons.append(InlineKeyboardButton(text=f"{i} Страница",
                                               callback_data=f"bookmarks_{i}"))

    # Добавляем кнопки delete и cancel
    cancel_red_buttons: list[InlineKeyboardButton] = [
        InlineKeyboardButton(text=LEXICON['edit_bookmarks_button'], callback_data='edit_bookmarks_button'),
        InlineKeyboardButton(text=LEXICON['cancel'], callback_data='cancel')]

    bookmarks_builder.row(*bm_buttons, width=1)
    bookmarks_builder.row(*cancel_red_buttons)

    return bookmarks_builder


# builder с кнопками для удаления из bookmarks при выборе
def delete_bookmarks(indi, bm_list):
    delete_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    delete_buttons: list[InlineKeyboardButton] = []

    # Заполняем list Inline кнопками
    for i in sorted(bm_list):
        delete_buttons.append(InlineKeyboardButton(text=f"{LEXICON['del']} {i} Страница",
                                                   callback_data=f"del_{i}"))

    cancel_button: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON['cancel'], callback_data='cancel_del')

    delete_builder.row(*delete_buttons, width=1)
    delete_builder.row(cancel_button)

    return delete_builder
