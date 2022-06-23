from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from telegram import ChatAction

INPUT_TEXT = 0
wins_totales = 0

USER_TOKEN = 'User Token'

def start(update, context):
    update.message.reply_text('Noche de puro Wins !')

def win_command_handler(update, context):
    update.message.reply_text('Cuantas Wins deseas agregar ?')
    return INPUT_TEXT


def agregar_win(numero_win):
    global wins_totales
    wins_totales += int(numero_win)

# def quitar_win(numero_win):
#     global wins_totales
#     wins_totales -= int(numero_win)

def input_text (update, context):
    text = update.message.text
    agregar_win(text)
    update.message.reply_text('Wins totales: ' + str(wins_totales))

    return ConversationHandler.END

if __name__ == '__main__':
    # Crea el updater y le pasa el token del bot
    updater = Updater(token=USER_TOKEN, use_context=True)
    dp = updater.dispatcher #se encarga de enviar los mensajes

    # Crea el comando start y lo agrega al dispatcher
    dp.add_handler(CommandHandler('start', start))

    dp.add_handler(ConversationHandler(
        entry_points=[CommandHandler('win', win_command_handler)],

        states={
            INPUT_TEXT: [MessageHandler(Filters.text, input_text)]
        },

        fallbacks=[]
    ))

    #add handlers
    updater.start_polling()
    updater.idle()

   