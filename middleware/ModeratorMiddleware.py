from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from Config import ADMIN
from database.UserType import UserTypeService
from database.Users import UsersService

users_service = UsersService()
user_type_service = UserTypeService()


class ModeratorMiddleware(BaseMiddleware):
    def __init__(self):
        self.user_type = user_type_service.getModeratorType()

    async def __call__(self, handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], event: TelegramObject,
                       data: Dict[str, Any]) -> Any:
        user = users_service.getById(event.from_user.id)
        if event.from_user.id != ADMIN and (user is None or user['user_type'] != self.user_type):
            await event.bot.send_message(event.from_user.id, "Вы не являетесь модератором!")
            return

        return await handler(event, data)
