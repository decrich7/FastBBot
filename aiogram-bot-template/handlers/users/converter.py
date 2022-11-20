# -*- coding: utf-8 -*-
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram import types
from aiogram import Dispatcher
from urllib.request import urlopen
from urllib.request import urlretrieve
import cgi
import logging
import os
from pathlib import Path
from .frx_t import converter
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
import requests
from keyboards.inline.format_files import formats
from loader import dp
from states.conver_state import State_frx

@dp.callback_query_handler(text_contains="convert_frx")
async def convert_frx(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Конвертирование из FRX в различные форматы\n"
                              "Пришлите боту файл с расширением frx")

    await State_frx.await_file.set()


@dp.message_handler(state=State_frx.await_file, content_types=types.ContentType.DOCUMENT)
async def frx_to_other_format(message: types.Message, state: FSMContext):
    path_to_download = Path().joinpath("files_frx")
    path_to_download.mkdir(parents=True, exist_ok=True)
    path_to_download = path_to_download.joinpath(message.document.file_name)
    await message.document.download(destination=path_to_download)
    await message.answer(f"Выберите ", reply_markup=formats)
    await state.update_data(path=f'./files_frx/{message.document.file_name}')
    await state.update_data(name=f'{message.document.file_name}')

    await State_frx.choice_form.set()


@dp.callback_query_handler(state=State_frx.choice_form)
async def convert_frx(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    callback_data = call.data.split('_')[-1]
    data = await state.get_data()
    path = data.get("path")
    name = data.get('name')
    print(callback_data)
    print(path)
    converter(path, callback_data)

    await call.message.answer_document(document=types.InputFile(f'./files_frx/{name.split(".")[0]}.{callback_data}'))




