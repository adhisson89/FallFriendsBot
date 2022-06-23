from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text('Noche de puro Wins !')


if __name__ == '__main__':
    # Crea el updater y le pasa el token del bot
    updater = Updater(token='TOKEN', use_context=True)
    dp = updater.dispatcher #se encarga de enviar los mensajes

    dp.add_handler(CommandHandler('start', start))

    #add handlers
    updater.start_polling()
    updater.idle()

   