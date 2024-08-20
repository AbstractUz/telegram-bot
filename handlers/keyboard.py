from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Config import DEFAULT_LANGUAGE, INSTAGRAM_URL
from database.Categories import CategoriesService
from database.CategoryType import CategoryTypeService
from handlers.Translation import _

category_types_service = CategoryTypeService()
categories_service = CategoriesService()
_lang = DEFAULT_LANGUAGE


def all_category_types(lang_=_lang, prefix=""):
    category_types = category_types_service.getAllCategoryTypes()
    rows = []
    for category_type in category_types:
        row = [InlineKeyboardButton(text=f"{category_type[f'name_{lang_}']}",
                                    callback_data=f"{prefix}category_type:{category_type['id']}")]
        rows.append(row)
    return InlineKeyboardMarkup(inline_keyboard=rows)


def all_categories(prefix="", category_type_id=None):
    categories = categories_service.getByType(category_type_id)
    rows = []
    for category in categories:
        row = [InlineKeyboardButton(text=f"{category['name']}", callback_data=f"{prefix}category:{category['id']}")]
        rows.append(row)
    return InlineKeyboardMarkup(inline_keyboard=rows)


def admin_moderators_main_menu(lang_=_lang):
    row1 = [
        InlineKeyboardButton(text=_('Все модераторы', lang_), callback_data='all_moderators'),
        InlineKeyboardButton(text=_('Добавить модератора', lang_), callback_data='add_moderator'),
        InlineKeyboardButton(text=_('Удалить модератора', lang_), callback_data='remove_moderator')
    ]
    row2 = [
        InlineKeyboardButton(text=_('Главное меню', lang_), callback_data='main_menu')
    ]
    rows = [row1, row2]
    return InlineKeyboardMarkup(inline_keyboard=rows)


def admin_categories_main_menu(lang_=_lang):
    row1 = [
        InlineKeyboardButton(text=_('Все категории', lang_), callback_data='all_categories'),
        InlineKeyboardButton(text=_('Добавить категорию', lang_), callback_data='add_category'),
        InlineKeyboardButton(text=_('Удалить категорию', lang_), callback_data='remove_category')
    ]
    row2 = [
        InlineKeyboardButton(text=_('Главное меню', lang_), callback_data='main_menu')
    ]
    rows = [row1, row2]
    return InlineKeyboardMarkup(inline_keyboard=rows)


def admin_main_menu(lang_=_lang):
    row1 = [
        InlineKeyboardButton(text=_('Модераторы', lang_), callback_data='moderators'),
    ]
    row2 = [
        InlineKeyboardButton(text=_('Типы категорий', lang_), callback_data='category_types'),
    ]
    row3 = [
        InlineKeyboardButton(text=_('Категории', lang_), callback_data='categories'),
    ]
    row4 = [
        InlineKeyboardButton(text=_('Заказы', lang_), callback_data='orders'),
    ]
    row5 = [
        InlineKeyboardButton(text=_('Отмена', lang_), callback_data='cancel')
    ]
    rows = [row1, row2, row3, row4, row5]
    return InlineKeyboardMarkup(inline_keyboard=rows)


def back_to_moderators_menu(lang_=_lang):
    row = [InlineKeyboardButton(text=_('Назад', lang_), callback_data='moderators')]
    rows = [row]
    return InlineKeyboardMarkup(inline_keyboard=rows)


def back_to_category_types_menu(lang_=_lang):
    row = [InlineKeyboardButton(text=_('Назад', lang_), callback_data='category_types')]
    rows = [row]
    return InlineKeyboardMarkup(inline_keyboard=rows)


def back_to_categories_menu(lang_=_lang):
    row = [InlineKeyboardButton(text=_('Назад', lang_), callback_data='categories')]
    rows = [row]
    return InlineKeyboardMarkup(inline_keyboard=rows)


def cancel_button(lang_=_lang):
    row = [InlineKeyboardButton(text=_('Отмена', lang_), callback_data='cancel')]
    rows = [row]
    return InlineKeyboardMarkup(inline_keyboard=rows)


def person_count(lang_=_lang):
    row = [
        InlineKeyboardButton(text=_('Один человек', lang_), callback_data='single_person'),
        InlineKeyboardButton(text=_('Несколько человек', lang_), callback_data='multiple_person')
    ]
    rows = [row]
    return InlineKeyboardMarkup(inline_keyboard=rows)


def instagram_button(lang_=_lang):
    row = [InlineKeyboardButton(text=_('Подписаться', lang_), url=INSTAGRAM_URL)]
    rows = [row]
    return InlineKeyboardMarkup(inline_keyboard=rows)


def order_accept(order_id, lang_=_lang):
    row = [
        InlineKeyboardButton(text=_('Принять', lang_), callback_data=f'accept_order:{order_id}')
    ]
    rows = [row]
    return InlineKeyboardMarkup(inline_keyboard=rows)


def category_type_menu(lang_=_lang):
    rows = [
        [
            InlineKeyboardButton(text=_('Все типы категорий', lang_), callback_data='all_category_types'),
        ],
        [
            InlineKeyboardButton(text=_('Добавить тип категории', lang_), callback_data='add_category_type'),
        ],
        [
            InlineKeyboardButton(text=_('Удалить тип категории', lang_), callback_data='remove_category_type'),
        ],
        [
            InlineKeyboardButton(text=_('Главное меню', lang_), callback_data='main_menu')
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=rows)


def language_markup():
    rows = [
        [
            InlineKeyboardButton(text='O\'zbek', callback_data='lang_uz'),
            InlineKeyboardButton(text='Русский', callback_data='lang_ru'),
            InlineKeyboardButton(text='English', callback_data='lang_en')
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=rows)
