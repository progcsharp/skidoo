from aiogram import Dispatcher

from State.form import Form
from handler.message import message_form


async def register_handlers_message(dp: Dispatcher):
    dp.message.register(message_form, Form.waiting_for_issue)
