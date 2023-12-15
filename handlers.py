from telegram.ext import CallbackContext
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton


LIKES, DISLIKES = 0, 0


def start(update: Update, context: CallbackContext):
    user = update.message.from_user

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='👍'), KeyboardButton(text='👎')]
        ],
        resize_keyboard=True
    )
    update.message.reply_html(
        text=f'Hello, {user.full_name}! Press one of the buttons.',
        reply_markup=keyboard
    )

def like(update: Update, context: CallbackContext):
    global LIKES
    LIKES += 1

    update.message.reply_html(text=f'likes: {LIKES}\ndislikes: {DISLIKES}')


def dislike(update: Update, context: CallbackContext):
    global DISLIKES
    DISLIKES += 1

    update.message.reply_html(text=f'likes: {LIKES}\ndislikes: {DISLIKES}')
