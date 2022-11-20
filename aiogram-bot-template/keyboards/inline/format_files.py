# -*- coding: utf-8 -*-

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


formats = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="PDF", callback_data="format_pdf"),
        InlineKeyboardButton(text="XML", callback_data="format_xml"),
        InlineKeyboardButton(text="HTML", callback_data="format_html"),
        InlineKeyboardButton(text="Word", callback_data="format_docx"),

    ],
    [
        InlineKeyboardButton(text="Power Point", callback_data="format_pptx"),
        InlineKeyboardButton(text="Excel", callback_data="format_xlsx"),
        InlineKeyboardButton(text="RTF", callback_data="format_rtf"),
        InlineKeyboardButton(text="Open Writer", callback_data="format_odt"),

    ],
    [
        InlineKeyboardButton(text="Open Calc", callback_data="format_ods"),
        InlineKeyboardButton(text="Images", callback_data="format_png"),
        InlineKeyboardButton(text="SVG", callback_data="format_svg"),

    ]
])