# -*- coding: utf-8 -*-

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


private_office = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Личный Кабинет", callback_data="private_office")
    ],
    [
        InlineKeyboardButton(text="Конвертер FRX", callback_data="convert_frx")
    ]
])