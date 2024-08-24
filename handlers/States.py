from aiogram.fsm.state import StatesGroup, State


class OrderState(StatesGroup):
    category_type = State()
    message_ids = State()
    category = State()
    ceremony_date = State()
    single_person = State()
    photo_id = State()
    cheque_id = State()


class ModeratorState(StatesGroup):
    register_user_id = State()
    unregister_user_id = State()


class CategoryTypeState(StatesGroup):
    id = State()
    name_uz = State()
    name_ru = State()
    name_en = State()
    single_price = State()
    group_price = State()


class CategoryState(StatesGroup):
    name = State()
    photo = State()
    type_id = State()


class OrderPhotos(StatesGroup):
    order_id = State()
    photos = State()


class CancelOrder(StatesGroup):
    order_id = State()
    reason = State()
