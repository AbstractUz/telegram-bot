from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

admin_welcome = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🗄 Categories panel")
        ]

    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

welcome_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇿 O'zbek tili", callback_data="lang_uzb")
        ],
        [
            InlineKeyboardButton(text="🇷🇺 Русский язык", callback_data="lang_rus")
        ],
        [
            InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_eng")
        ]
    ]
)
uzb_types = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💒  To'yxona", callback_data="1")
        ],
        [
            InlineKeyboardButton(text="🏛 Restoran", callback_data="2")
        ]
    ]
)
rus_types = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💒  Свадебный зал", callback_data="1")
        ],
        [
            InlineKeyboardButton(text="🏛 Ресторан", callback_data="2")
        ]
    ]
)
eng_types = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💒  Wedding Hall", callback_data="1")
        ],
        [
            InlineKeyboardButton(text="🏛 Restaurant", callback_data="2")
        ]
    ]
)
toyla = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💒  A'lo", callback_data="restaurant_A'lo"),
            InlineKeyboardButton(text="💒  Sarbon", callback_data="restaurant_Sarbon")
        ],
        [
            InlineKeyboardButton(text="🔙", callback_data="back")
        ]
    ]
)
restoranla = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🏛 Bek", callback_data="restaurant_Bek")
        ],
        [
            InlineKeyboardButton(text="🔙", callback_data="back")
        ]
    ]
)
uzb_soni = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👤 Bitta odam", callback_data="quantity_one")
        ],
        [
            InlineKeyboardButton(text="👥 Ko'pchilik", callback_data="quantity_many")
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="quantity_back")
        ]
    ]
)
rus_soni = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👤 Один человек", callback_data="quantity_one")
        ],
        [
            InlineKeyboardButton(text="👥 Общое фото", callback_data="quantity_many")
        ],
        [
            InlineKeyboardButton(text="🔙 Назад", callback_data="quantity_back")
        ]
    ]
)
eng_soni = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👤 One person", callback_data="quantity_one")
        ],
        [
            InlineKeyboardButton(text="👥 General photo", callback_data="quantity_many")
        ],
        [
            InlineKeyboardButton(text="🔙 Back", callback_data="quantity_back")
        ]
    ]
)
main_admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📑 Qabul qilingan arizalar", callback_data="spisok")
        ],
        [
            InlineKeyboardButton(text="🔙", callback_data="back")
        ]
    ]
)
admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Tasdiqlash", callback_data="admit")
        ],
        [
            InlineKeyboardButton(text="❌ Bekor qilish", callback_data="cancel")
        ]
    ]
)
admin_types = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💒  To'yxona", callback_data="1")
        ],
        [
            InlineKeyboardButton(text="🏛 Restoran", callback_data="2")
        ],
        [
            InlineKeyboardButton(text="🗄 Admin panel", callback_data="admin")
        ]
    ]
)
