from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from database.Categories import CategoriesService
from database.CategoryType import CategoryTypeService
from database.UserType import UserTypeService
from database.Users import UsersService
from handlers.keyboard import admin_main_menu, admin_moderators_main_menu, back_to_moderators_menu, cancel_button, \
    admin_categories_main_menu, category_type_menu, back_to_category_types_menu, all_category_types, \
    back_to_categories_menu
from middleware.Middleware import AdminMiddleware, ModeratorMiddleware
from handlers.States import ModeratorState, CategoryTypeState, CategoryState
from handlers.Translation import _

route = Router()
route.message.middleware.register(AdminMiddleware())

users_service = UsersService()
user_type_service = UserTypeService()
category_type_service = CategoryTypeService()
categories_service = CategoriesService()


async def command_start_handler(message: Message, lang: str) -> None:
    await message.answer(_("Главное меню!", lang), reply_markup=admin_main_menu(lang))


@route.callback_query(
    F.data == 'add_moderator'
)
async def add_moderator(query: CallbackQuery, state: FSMContext, lang: str) -> None:
    await state.set_state(ModeratorState.register_user_id)
    await query.message.answer(_("Введите ID пользователя, которого хотите сделать модератором!", lang), reply_markup=cancel_button(lang))


@route.message(
    ModeratorState.register_user_id
)
async def add_moderator_id(message: Message, state: FSMContext, lang: str) -> None:
    await state.update_data(user_id=message.text)
    data = await state.get_data()
    user = users_service.getById(data['user_id'])
    if user is None:
        await message.answer(_("Пользователь не найден!", lang))
        return
    users_service.updateUserType(user['id'],  user_type_service.getModeratorType())
    await state.clear()
    await message.answer(_("Пользователь успешно добавлен в модераторы!", lang), reply_markup=admin_moderators_main_menu(lang))
# END REGISTER MODERATOR


# BEGIN UNREGISTER MODERATOR
@route.callback_query(
    F.data == 'remove_moderator'
)
async def remove_moderator(query: CallbackQuery, state: FSMContext, lang: str) -> None:
    await state.set_state(ModeratorState.unregister_user_id)
    await query.message.answer(_("Введите ID пользователя, которого хотите убрать из модераторов!", lang), reply_markup=cancel_button(lang))


@route.message(
    ModeratorState.unregister_user_id
)
async def remove_moderator_id(message: Message, state: FSMContext, lang: str) -> None:
    await state.update_data(user_id=message.text)
    data = await state.get_data()
    user = users_service.getById(data['user_id'])
    if user is None:
        await message.answer(_("Пользователь не найден!", lang))
        return
    users_service.updateUserType(user['id'],  user_type_service.getCustomerType())
    await state.clear()
    await message.answer(_("Пользователь успешно убран из модераторов!", lang), reply_markup=admin_moderators_main_menu(lang))


@route.callback_query(
    F.data == 'all_moderators'
)
async def all_users(query: CallbackQuery, lang: str) -> None:
    users = users_service.getAllByUserType(user_type_service.getModeratorType())
    text = ""
    if not users:
        await query.answer(_("Модераторов нет!", lang))
        return

    for user in users:
        text += f"ID: {user['id']}\nUsername: {user['username']}\n\n"
    await query.message.edit_text(text, reply_markup=back_to_moderators_menu(lang))


@route.callback_query(
    F.data == 'moderators'
)
async def moderators(query: CallbackQuery, lang: str) -> None:
    await query.message.edit_text(_("Модераторы", lang), reply_markup=admin_moderators_main_menu(lang))


@route.callback_query(
    F.data == 'category_types'
)
async def category_types(query: CallbackQuery, lang: str) -> None:
    await query.message.edit_text(_("Category types!", lang), reply_markup=category_type_menu(lang))


@route.callback_query(
    F.data == 'add_category_type'
)
async def add_category_type(query: CallbackQuery, state: FSMContext, lang: str) -> None:
    await state.set_state(CategoryTypeState.name_uz)
    await query.message.answer(_("Введите название категории на узбекском языке!", lang), reply_markup=cancel_button(lang))


@route.message(
    CategoryTypeState.name_uz
)
async def add_category_name(message: Message, state: FSMContext, lang: str) -> None:
    await state.update_data(name_uz=message.text)
    await state.set_state(CategoryTypeState.name_ru)
    await message.answer(_("Введите название категории на русском языке!", lang))


@route.message(
    CategoryTypeState.name_ru
)
async def add_category_name(message: Message, state: FSMContext, lang: str) -> None:
    await state.update_data(name_ru=message.text)
    await state.set_state(CategoryTypeState.name_en)
    await message.answer(_("Введите название категории на английском языке!", lang))


@route.message(
    CategoryTypeState.name_en
)
async def add_category_name(message: Message, state: FSMContext, lang: str) -> None:
    await state.update_data(name_en=message.text)
    await state.set_state(CategoryTypeState.single_price)
    await message.answer(_("Введите цену за одного человека!", lang))


@route.message(
    CategoryTypeState.single_price
)
async def add_category_single_price(message: Message, state: FSMContext, lang: str) -> None:
    if (not message.text.isdigit()) or int(message.text) < 0:
        await message.answer(_("Неправильная цена!", lang))
        return
    await state.update_data(single_price=message.text)
    await state.set_state(CategoryTypeState.group_price)
    await message.answer(_("Введите цену за группу!", lang))


@route.message(
    CategoryTypeState.group_price
)
async def add_category_group_price(message: Message, state: FSMContext, lang: str) -> None:
    if (not message.text.isdigit()) or int(message.text) < 0:
        await message.answer(_("Неправильная цена!", lang))
        return
    await state.update_data(group_price=message.text)
    data = await state.get_data()
    category_type_service.createCategoryType(data['name_uz'], data['name_ru'], data['name_en'], data['single_price'], data['group_price'])
    await state.clear()
    await message.answer(_("Категория успешно добавлена!", lang), reply_markup=category_type_menu(lang))


@route.callback_query(
    F.data == 'all_category_types'
)
async def get_all_category_types(query: CallbackQuery, lang: str) -> None:
    category_types = category_type_service.getAllCategoryTypes()
    text = ""
    for category_type in category_types:
        text += f"ID: {category_type['id']}\nName: {category_type['name_uz']}\nSingle price: {category_type['single_price']} so'm\nGroup price: {category_type['group_price']} so'm\n\n"

    if text == "":
        await query.answer(_("Категорий нет!", lang))
        return

    await query.message.edit_text(text, reply_markup=back_to_category_types_menu(lang), parse_mode='Markdown')


@route.callback_query(
    F.data == 'remove_category_type'
)
async def remove_category(query: CallbackQuery, state: FSMContext, lang: str) -> None:
    await state.set_state(CategoryTypeState.id)
    await query.message.answer(_("Введите ID категории, которую хотите удалить!", lang), reply_markup=cancel_button(lang))


@route.message(
    CategoryTypeState.id
)
async def remove_category_id(message: Message, state: FSMContext, lang: str) -> None:
    await state.update_data(id=message.text)
    data = await state.get_data()
    result = category_type_service.deleteCategoryType(data['id'])

    if result is None:
        await message.answer(_("Категория не найдена!", lang))
        return

    await state.clear()
    await message.answer(_("Категория успешно удалена!", lang), reply_markup=category_type_menu(lang))


@route.callback_query(
    F.data == 'categories'
)
async def categories(query: CallbackQuery, lang: str) -> None:
    await query.message.edit_text(_("Categories!", lang), reply_markup=admin_categories_main_menu(lang))


@route.callback_query(
    F.data == 'add_category'
)
async def add_category(query: CallbackQuery, state: FSMContext, lang: str) -> None:
    await state.set_state(CategoryState.name)
    await query.message.answer(_("Введите название категории!", lang), reply_markup=cancel_button(lang))


@route.message(
    CategoryState.name
)
async def add_category_name(message: Message, state: FSMContext, lang: str) -> None:
    await state.update_data(name=message.text)
    await state.set_state(CategoryState.photo)
    await message.answer(_("Отправьте фото категории!", lang))


@route.message(
    CategoryState.photo
)
async def add_category_photo(message: Message, state: FSMContext, lang: str) -> None:
    await state.update_data(photo=message.photo[-1].file_id)
    await state.set_state(CategoryState.type_id)
    await message.answer(_("Введите типа категории!", lang), reply_markup=all_category_types(lang))


@route.callback_query(
    F.data.startswith('category_type:')
)
async def add_category_type_id(query: CallbackQuery, state: FSMContext, lang: str) -> None:
    category_type_id = query.data.split(':')[-1]
    await state.update_data(type_id=category_type_id)
    data = await state.get_data()
    categories_service.create(data['name'], data['photo'], data['type_id'])
    await state.clear()
    await query.message.answer(_("Категория успешно добавлена!", lang), reply_markup=admin_categories_main_menu(lang))


@route.callback_query(
    F.data == 'all_categories'
)
async def all_categories(query: CallbackQuery, lang: str) -> None:
    categories = categories_service.getAll()
    text = ""
    for category in categories:
        category_type = category_type_service.getById(category['category_type'])
        text += f"ID: {category['id']}\nName: {category['name']}\nType: {category_type[f'name_{lang}']}\nPrice single: {category_type['single_price']}\nPrice group: {category_type['group_price']}\n"

    if text == "":
        await query.answer(_("Категорий нет!", lang))
        return

    await query.message.edit_text(text, reply_markup=back_to_categories_menu(lang))


@route.callback_query(
    F.data == 'main_menu'
)
async def main_menu(query: CallbackQuery, lang: str) -> None:
    await query.message.edit_text(_("Главное меню!", lang), reply_markup=admin_main_menu(lang))


@route.callback_query(
    F.data == 'cancel'
)
async def cancel(query: CallbackQuery, state: FSMContext, lang: str) -> None:
    await state.clear()
    await query.message.delete()