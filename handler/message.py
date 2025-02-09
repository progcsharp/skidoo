from aiogram import types
from aiogram.fsm.context import FSMContext

from config import bot, ADMIN_ID


async def message_form(message: types.Message, state: FSMContext):
    await bot.send_message(ADMIN_ID, f"Сообщение от пользователя: @{message.from_user.username}\nСообщение: {message.text}")
    await state.clear()
    await message.answer("Спасибо за ваше сообщение! Мы рассмотрим вашу проблему.")
