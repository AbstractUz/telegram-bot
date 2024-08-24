from aiogram import Router
from aiogram.filters import Command

from middleware.ModeratorMiddleware import ModeratorMiddleware

router = Router()
router.message.middleware.register(ModeratorMiddleware())


@router.message(
    Command("moderator")
)
async def moderator_hello(message):
    await message.answer("Hello, Moderator!")