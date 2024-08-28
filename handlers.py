from telegram.ext import CallbackContext
from telegram import Update
from keyboards import keyboard, inline_keyboard
from db import(
    is_user,
    add_user,
    get_user,
    inc_like,
    inc_dislike,
    clear,
    inc_inline_like,
    inc_inline_dislike,
    inline_clear,
)


def start(update: Update, context: CallbackContext):
    id = update.effective_user.id
    first_name = update.message.chat.first_name
    if not is_user(chat_id=str(id)):
        add_user(chat_id=str(id))
        update.message.reply_text(
        text=f'Hello, {first_name}! Press one of the buttons.',
        )
    else:
        user_data = get_user(chat_id=str(id))
        update.message.reply_text(
        text=f'Hello, {first_name}! Press one of the buttons.',
        )

def like(update: Update, context: CallbackContext):
    user = update.effective_user
    
    if not is_user(str(user.id)):
        start(update,context)
        return
    inc_like(chat_id=str(user.id))

    user_data = get_user(chat_id=str(user.id))
    update.message.reply_html(
        text=f'<b>🔥 likes:</b> {user_data["likes"]}\n<b>💣 dislikes:</b> {user_data["dislikes"]}',
        reply_markup=keyboard
    )
    update.message.reply_html(
            text=f'<b>🔥 inline likes:</b> {user_data["inline_likes"]}\n<b>💣 inline dislikes:</b> {user_data["inline_dislikes"]}',
            reply_markup=inline_keyboard
    )

def dislike(update: Update, context: CallbackContext):
    user = update.effective_user
    
    if not is_user(str(user.id)):
        start(update,context)
        return
    inc_dislike(chat_id=str(user.id))

    user_data = get_user(chat_id=str(user.id))
    update.message.reply_html(
        text=f'<b>🔥 likes:</b> {user_data["likes"]}\n<b>💣 dislikes:</b> {user_data["dislikes"]}',
        reply_markup=keyboard
    )
    update.message.reply_html(
            text=f'<b>🔥 inline likes:</b> {user_data["inline_likes"]}\n<b>💣 inline dislikes:</b> {user_data["inline_dislikes"]}',
            reply_markup=inline_keyboard
    )

def add_clear(update: Update, context: CallbackContext):
    user = update.effective_user

    if not is_user(str(user.id)):
        start(update,context)
        return
    clear(chat_id=str(user.id))

    user_data = get_user(chat_id=str(user.id))
    update.message.reply_html(
        text=f"<b>🔥 likes:</b> {user_data['likes']}\n<b>💣 dislikes:</b> {user_data['dislikes']}",
        reply_markup=keyboard
    )
    update.message.reply_html(
            text=f'<b>🔥 inline likes:</b> {user_data["inline_likes"]}\n<b>💣 inline dislikes:</b> {user_data["inline_dislikes"]}',
            reply_markup=inline_keyboard
    )

def photo_like_dislike(update: Update, context: CallbackContext):
    user = update.effective_user
    file = update.message.photo[0].file_id
    if not is_user(str(user.id)):
        start(update,context)
        return
    user_data = get_user(chat_id=str(user.id))
    update.message.reply_photo(
        photo=file,
        caption = f'🔥 inline likes: {user_data["inline_likes"]}\n💣 inline dislikes: {user_data["inline_dislikes"]}', 
        reply_markup=inline_keyboard)
    

def photo_like_results(update: Update, context: CallbackContext):
    emoji_type = update.callback_query.data.split(':')[1]
    user = update.effective_user
    user_data = get_user(chat_id=str(user.id))

    if emoji_type == 'inline_like':
        inc_inline_like(chat_id=str(user.id))
    elif emoji_type == 'inline_dislike':
        inc_inline_dislike(chat_id=str(user.id))
    else:
        inline_clear(chat_id=str(user.id))

    new_caption = (f'🔥 inline likes: {user_data["inline_likes"]}\n'
                   f'💣 inline dislikes: {user_data["inline_dislikes"]}\n')

    current_caption = update.callback_query.message.caption

    if current_caption != new_caption:
        update.callback_query.message.edit_caption(
            caption=new_caption,
            reply_markup=inline_keyboard,
        )
       


def inline_like(update: Update, context: CallbackContext):
    user = update.effective_user

    if not is_user(str(user.id)):
        start(update, context)
        return

    inc_inline_like(chat_id=str(user.id))

    user_data = get_user(chat_id=str(user.id))
    context.bot.edit_message_text(
        chat_id=user.id,
        message_id=update.callback_query.message.message_id,
        text=f'<b>🔥 inline likes:</b> {user_data["inline_likes"]}\n<b>💣 inline dislikes:</b> {user_data["inline_dislikes"]}',
        reply_markup=inline_keyboard,
        parse_mode='HTML'
    )

def inline_dislike(update: Update, context: CallbackContext):
    user = update.effective_user

    if not is_user(str(user.id)):
        start(update,context)
        return
    
    inc_inline_dislike(chat_id=str(user.id))

    user_data = get_user(chat_id=str(user.id))
    context.bot.edit_message_text(
        chat_id = user.id,
        message_id = update.callback_query.message.message_id,
        text = f"<b>🔥 inline likes:</b> {user_data['inline_likes']}\n<b>💣 inline dislikes:</b> {user_data['inline_dislikes']}",
        reply_markup = inline_keyboard,
        parse_mode = "HTML"
    )

def inline_like_dislike_clear(update: Update, context: CallbackContext):
    user = update.effective_user
    if not is_user(str(user.id)):
        start(update,context)
        return
    inline_clear(chat_id=(str(user.id)))

    user_data = get_user(chat_id=str(user.id))
    context.bot.edit_message_text(
        chat_id = user.id,
        message_id = update.callback_query.message.message_id,
        text = f"<b>🔥 inline likes:</b> {user_data['inline_likes']}\n<b>💣 inline_dislikes:</b> {user_data['inline_dislikes']}",
        reply_markup = inline_keyboard,
        parse_mode = "HTML"
    )

