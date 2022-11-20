# -*- coding: utf-8 -*-

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.button_private_office import private_office
from loader import dp
from keyboards.inline.webapp_buttons import menu, menu_2_0


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}! \n"
                         f"FastBBot - это сервис позволяющий вести быстрый и просто документооборот", reply_markup=private_office)


from aiogram.types import Message, CallbackQuery


@dp.callback_query_handler(text_contains="private_office")
async def buying_pear(call: CallbackQuery):
    # Обязательно сразу сделать answer, чтобы убрать "часики" после нажатия на кнопку.
    # Укажем cache_time, чтобы бот не получал какое-то время апдейты, тогда нижний код не будет выполняться.
    await call.answer(cache_time=60)

    await call.message.answer("Здесь вы можете работать(дальше не придумал 🙍🏿‍♀️)",
                              reply_markup=menu_2_0)
