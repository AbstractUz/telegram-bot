from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.dispatcher.middlewares.user_context import UserContextMiddleware
from aiogram.types import TelegramObject, CallbackQuery, InlineQuery, Update
from aiogram.utils.callback_answer import CallbackAnswerMiddleware

from Config import ADMIN
from database.UserType import UserTypeService
from database.Users import UsersService

available_languages = ('uz', 'ru', 'en')

users_service = UsersService()
user_type_service = UserTypeService()

class Middleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        user = None
        try:
            message = event['message']
            query = event['callback_query']['message']
            user_id = message['from_user']['id'] if message else query['from_user']['id']
            user = users_service.getById(user_id)
        except:
            pass

        if user is not None:
            data['lang'] = user['lang']
        else:
            data['lang'] = 'uz'
        return await handler(event, data)


class AdminMiddleware(BaseMiddleware):
    async def __call__(self, handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], event: TelegramObject,
                       data: Dict[str, Any]) -> Any:
        if event.from_user.id != ADMIN:
            await event.bot.send_message(event.from_user.id, "Вы не являетесь администратором!")
            return

        return await handler(event, data)


class ModeratorMiddleware(BaseMiddleware):
    async def __call__(self, handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], event: TelegramObject,
                       data: Dict[str, Any]) -> Any:
        user = users_service.getById(event.from_user.id)
        if user is None or user['user_type'] != user_type_service.getModeratorType():
            await event.bot.send_message(event.from_user.id, "Вы не являетесь модератором!")
            return

        return await handler(event, data)