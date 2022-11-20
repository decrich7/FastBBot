# -*- coding: utf-8 -*-
from aiogram.types import ContentTypes, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram import types
from aiogram import Dispatcher
from urllib.request import urlopen
from urllib.request import urlretrieve
import cgi
import urllib3

import logging
import os
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
import requests
from keyboards.inline.webapp_buttons import templates1, exports1, reports1, data_sources1, data_sources1, group1, \
    users1, api_key1
from loader import dp

from aiogram.types import WebAppData


# @dp.callback_query_handler(text_contains="templates")
# async def templates(call: CallbackQuery):
#     await call.answer(cache_time=60)
#     await call.message.answer("На этой WEB-Странице вы можете работать с шаблонами ", reply_markup=templates1)
#
#
# @dp.callback_query_handler(text_contains="exports")
# async def exports(call: CallbackQuery):
#     await call.answer(cache_time=60)
#     await call.message.answer("На этой WEB-Странице вы можете работать с экспортами ",
#                               reply_markup=exports1)
#
#
# @dp.callback_query_handler(text_contains="reports")
# async def reports(call: CallbackQuery):
#     await call.answer(cache_time=60)
#     await call.message.answer("На этой WEB-Странице вы можете работать с отчётами",
#                               reply_markup=reports1)
#
#
# @dp.callback_query_handler(text_contains="data_sources")
# async def buying_pear(call: CallbackQuery):
#     await call.answer(cache_time=60)
#     await call.message.answer("На этой WEB-Странице вы можете работать с Источниками данных",
#                               reply_markup=data_sources1)
#
#
# @dp.callback_query_handler(text_contains="group")
# async def buying_pear(call: CallbackQuery):
#     await call.answer(cache_time=60)
#     await call.message.answer("На этой WEB-Странице вы можете работать с Группами ",
#                               reply_markup=group1)
#
#
# @dp.callback_query_handler(text_contains="users")
# async def buying_pear(call: CallbackQuery):
#     await call.answer(cache_time=60)
#     await call.message.answer("На этой WEB-Странице вы можете работать с Пользователями ",
#                               reply_markup=users1)
#
#
# @dp.callback_query_handler(text_contains="api_key")
# async def buying_pear(call: CallbackQuery):
#     await call.answer(cache_time=60)
#     await call.message.answer("На этой WEB-Странице вы можете работать с API Ключами ",
#                               reply_markup=api_key1)


async def send_file(dp: Dispatcher, q):
    id, name = str(q['web_app_data']['data']).split('|')
    # await dp.bot.send_message(q['from']['id'], f"https://fastreport.cloud/download/r/{id}")
    # r = requests.get(f"https://fastreport.cloud/download/r/{id}")

    with open(f'./files/{name}', 'wb') as f:
        f.write(requests.get(f"https://fastreport.cloud/download/r/{id}").content)

    await dp.bot.send_document(q['from']['id'], document=types.InputFile(f'./files/{name}'))



async def send_file_export(dp: Dispatcher, q):
    auth = urllib3.util.make_headers(
        basic_auth='apikey' + ':' + 'yuptozbh36s5uj1qkojexo5w91snjjmcw3sya8s84zy8t8yjow9y'
    ).get('authorization')

    headers = {
        'accept': 'application/json',
        'Authorization': auth
    }

    name, none = str(q['web_app_data']['data']).split('|')
    # await dp.bot.send_message(q['from']['id'], f"https://fastreport.cloud/download/r/{id}")
    root = requests.get(f"https://fastreport.cloud/api/rp/v1/Exports/Root?subscriptionId=6377865f5f620ebfce9a07ce", headers=headers).json()['id']
    print(root)
    list_files = requests.get(f"https://fastreport.cloud/api/rp/v1/Exports/Folder/{root}/ListFolderAndFiles?skip=0&take=100&subscriptionId=6377865f5f620ebfce9a07ce", headers=headers).json()['files']
    for i in list_files:
        print(i['name'].split('.')[0])
        if i['name'].split('.')[0] == name:
            with open(f'./files/{name}', 'wb') as f:
                f.write(requests.get(f"https://fastreport.cloud/download/r/{i['id']}").content)

            await dp.bot.send_document(q['from']['id'], document=types.InputFile(f'./files/{name}'))



@dp.message_handler(content_types=ContentTypes.WEB_APP_DATA)
async def cmd_start1(q: WebAppData):
    print(q)
    if str(q['web_app_data']['data']).split('|')[-1] == 'exp':
        await send_file_export(dp, q)
    else:
        await send_file(dp, q)
