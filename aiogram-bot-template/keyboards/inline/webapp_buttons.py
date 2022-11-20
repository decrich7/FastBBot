# -*- coding: utf-8 -*-

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import (
    MenuButtonWebApp,
    Message,
    WebAppInfo,
)
HOST = 'https://f601-37-145-228-41.eu.ngrok.io/'

menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Шаблоны", callback_data="templates"),
        InlineKeyboardButton(text="Отчёты", callback_data="reports"),
        InlineKeyboardButton(text="Экспорты", callback_data="exports")
    ],
    [
        InlineKeyboardButton(text="Источники", callback_data="data_sources"),
        InlineKeyboardButton(text="Группы", callback_data="group"),
        InlineKeyboardButton(text="Пользователи", callback_data="users")
    ],
    [
        InlineKeyboardButton(text="API ключи", callback_data="api_key")
    ]
])



menu_2_0 =  ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Шаблоны", web_app=WebAppInfo(url=f"{HOST}shablon/")),
            KeyboardButton(text="Отчеты", web_app=WebAppInfo(url=f"{HOST}reports/")),
            KeyboardButton(text="Экспорты", web_app=WebAppInfo(url=f"{HOST}exports/"))
        ],
        [
            KeyboardButton(text="Источники данных", web_app=WebAppInfo(url=f"{HOST}data/")),
            KeyboardButton(text="Группы", web_app=WebAppInfo(url=f"{HOST}reports/")),
            KeyboardButton(text="Пользователи", web_app=WebAppInfo(url=f"{HOST}users/"))
        ],
        [
            KeyboardButton(text="API ключи", web_app=WebAppInfo(url=f"{HOST}reports/"))
        ],
    ],
    resize_keyboard=True
)
# templates1 = InlineKeyboardMarkup(inline_keyboard=[
#     [
#         InlineKeyboardButton(text="Купи тут", web_app=WebAppInfo(url="https://sun9-1.userapi.com/impg/e0op5qZSdjtkfmW1UPHqYzN_PrA8b2uSSScFfA/4wG2Eg5tFvU.jpg?size=995x1920&quality=95&sign=1f55d77f54c30c262d8dd7eade979239&type=album"))
#     ]
# ])


templates1 = ReplyKeyboardMarkup(resize_keyboard=True).add(
                                  KeyboardButton(text="Шаблоны", web_app=WebAppInfo(
                                      url=f"{HOST}reports/")))

exports1 = ReplyKeyboardMarkup(resize_keyboard=True).add(
                                  KeyboardButton(text="Экспорты", web_app=WebAppInfo(
                                      url=f"{HOST}reports/")))

reports1 = ReplyKeyboardMarkup(resize_keyboard=True).add(
                                  KeyboardButton(text="Отчеты", web_app=WebAppInfo(
                                      url=f"{HOST}reports/")))

data_sources1 = ReplyKeyboardMarkup(resize_keyboard=True).add(
                                  KeyboardButton(text="Источники данных", web_app=WebAppInfo(
                                      url=f"{HOST}reports/")))

group1 = ReplyKeyboardMarkup(resize_keyboard=True).add(
                                  KeyboardButton(text="Группы", web_app=WebAppInfo(
                                      url=f"{HOST}reports/")))

users1 = ReplyKeyboardMarkup(resize_keyboard=True).add(
                                  KeyboardButton(text="Пользователи", web_app=WebAppInfo(
                                      url=f"{HOST}reports/")))

api_key1 = ReplyKeyboardMarkup(resize_keyboard=True).add(
                                  KeyboardButton(text="API ключи", web_app=WebAppInfo(
                                      url=f"{HOST}reports/")))


# pear_keyboard = InlineKeyboardMarkup(inline_keyboard=[
#     [
#         InlineKeyboardButton(text="Купи тут", url="https://rozetka.com.ua/champion_a00225/p27223057")
#     ]
# ])