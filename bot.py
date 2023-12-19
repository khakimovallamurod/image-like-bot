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
    inline_like,
    inline_dislike,
    inline_like_dislike_clear
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

    # add calback_query handlers
    dispatcher.add_handler(handler=CallbackQueryHandler(callback=inline_like,pattern="inline_like"))
    dispatcher.add_handler(handler=CallbackQueryHandler(callback=inline_dislike,pattern="inline_dislike"))
    dispatcher.add_handler(handler=CallbackQueryHandler(callback=inline_like_dislike_clear,pattern="inline_clear"))
    # start polling
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
