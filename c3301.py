from telegram import Update 
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler

button_help = 'Помощь'
heart_help = 'Диагностика рентгена грудной клетки'
exit_text = 'Выйти'

def button_help_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text = "Прости, я пока не могу тебе помочь",
        reply_markup = ReplyKeyboardRemove()
    )
def heart_help_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text = "Перед тем как мы начнём наш диалог скажу вот что: моя точность на относительно небольшом объёме тестовых пациентов составила 92%, поэтому не спеши с выводами",    
        reply_markup = ReplyKeyboardMarkup(
            keyboard = [
                [
                    KeyboardButton(text = exit_text)     
                ],
            ],
            resize_keyboard = True
        )
    )
def message_handler(update: Update, context: CallbackContext):
    text = update.message.text 
    if text == button_help:
        return button_help_handler(update = update, context = context)
    if text == heart_help:
        return heart_help_handler(update = update, context = context,)
    reply_markup = ReplyKeyboardMarkup(
            keyboard = [
                [
                    KeyboardButton(text = button_help), KeyboardButton(text = heart_help)
                    
                ],
            ],
            resize_keyboard = True
        )
    update.message.reply_text(
        text = 'Выберите одну из опций',  reply_markup = reply_markup  
    )
def main():
    updater = Updater( token = "1461952729:AAEsh0bccSBV1VNd9anhfbo3Tq-2StOiLTo", use_context=True)
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback = message_handler))
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()
