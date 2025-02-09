from aiogram import Dispatcher
from aiogram.filters import Command

from handler.commands import cmd_start, cmd_open, cmd_suggest, cmd_report_issue


async def register_handlers_commands(dp: Dispatcher):
    dp.message.register(cmd_start, Command('start'))
    dp.message.register(cmd_report_issue, Command('report_issue'))
    dp.message.register(cmd_suggest, Command('suggest'))
    dp.message.register(cmd_open, Command('open'))
