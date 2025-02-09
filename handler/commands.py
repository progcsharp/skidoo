from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder

from State.form import Form
from db.handler.create import create_user
from db.handler.get import get_user_by_tg_id


async def cmd_start(message: types.Message):

    if await get_user_by_tg_id(message.from_user.id):
        await create_user(tg_id=message.from_user.id, nickname=message.from_user.username)

    web_app_info = types.WebAppInfo(url="https://kbase-argroup.ru/places/")
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Открыть Веб-Приложение",
        web_app=web_app_info)
    )
    await message.answer('''Привет! Я — Skidoo, твой помощник в мире скидок! 🎉

С помощью меня ты можешь:

- 📩 /report_issue — сообщить о проблеме, с которой столкнулся.
- 💡 /suggest — предложить улучшение нашего сервиса, чтобы сделать его еще лучше для тебя!
- 🌐 /open — открыть веб-приложение и получить доступ ко всем скидкам и предложениям.

Если у тебя есть вопросы или нужна помощь, просто дай знать!''',
                         reply_markup=builder.as_markup())


async def cmd_report_issue(message: types.Message, state: FSMContext):
    await state.set_state(Form.waiting_for_issue)
    await message.answer("Пожалуйста, опишите вашу проблему как можно подробнее. Укажите, что именно не работает, и, если возможно, добавьте шаги для воспроизведения ошибки. Мы постараемся решить вашу проблему как можно быстрее!")


async def cmd_suggest(message: types.Message, state: FSMContext):
    await state.set_state(Form.waiting_for_issue)
    await message.answer("Пожалуйста, предложи улучшение нашего сервиса:")


async def cmd_open(message: types.Message):
    web_app_info = types.WebAppInfo(url="https://kbase-argroup.ru/places/")
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Открыть Веб-Приложение",
        web_app=web_app_info)
    )
    await message.answer('''Добро пожаловать в нашу централизованную систему скидок для студентов! Здесь вы сможете найти специальные предложения и скидки в различных заведениях.

Нажмите на кнопку ниже, чтобы открыть веб-приложение и начать экономить!''', reply_markup=builder.as_markup())
