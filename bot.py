from settings import get_token
from telegram.ext import (
    Updater, 
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler
)
from handlers import (
    start,
    like,
    dislike,
    add_clear,
    photo_like_dislike,
    photo_like_results
)


def main():
    TOKEN = get_token()

    # create udpater obj
    updater = Updater(TOKEN)
    
    # create dispatcher obj
    dispatcher = updater.dispatcher
    
    # add command handlers
    dispatcher.add_handler(handler=CommandHandler(command='start', callback=start))
    
    # add message handlers
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text('👍'), callback=like))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text('👎'), callback=dislike))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text('🆑'), callback=add_clear))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.photo, callback=photo_like_dislike))

    # add calback_query handlers
    dispatcher.add_handler(handler=CallbackQueryHandler(callback=photo_like_results,pattern="type_emoji:"))
    # start polling
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
