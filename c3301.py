from telegram import Update 
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler


def message_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text = 'Пример текста',
    )
def main():
    print('Start')

    updater = Updater(
        token = "1461952729:AAEsh0bccSBV1VNd9anhfbo3Tq-2StOiLTo",
        use_context=True
    )
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback = message_handler))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
