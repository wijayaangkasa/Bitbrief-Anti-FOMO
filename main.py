from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler,
    ConversationHandler, ContextTypes
)
from flask import Flask
from threading import Thread
import pandas as pd

# === STEP ===
GENDER, MOOD, BUDGET = range(3)

# === /start ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Cowok", callback_data='Pria')],
        [InlineKeyboardButton("Cewek", callback_data='Wanita')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Halo! Mau cari parfum yang cocok?\nPertama, kamu cewek atau cowok nih?", reply_markup=reply_markup)
    return GENDER

# === Gender Handler ===
async def pilih_gender(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    context.user_data["gender"] = query.data

    keyboard = [
        [InlineKeyboardButton("Kalem", callback_data='kalem')],
        [InlineKeyboardButton("Fresh", callback_data='fresh')],
        [InlineKeyboardButton("Dewasa", callback_data='dewasa')],
        [InlineKeyboardButton("Manis", callback_data='manis')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text("Lanjut ya!\nLagi pengen aroma yang gimana nih?", reply_markup=reply_markup)
