#!/usr/bin/env python

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def start(update: Update, _: CallbackContext):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hello and lets chat!')
    
def help_command(update: Update, _: CallbackContext):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help is on the way! Activate the dialogflow!')

def echo(update: Update, _: CallbackContext):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    with open('C:/Users/asylb/OneDrive/Documents/TLG/Python/api keys/telegramKey.txt', 'r') as f:
        token = f.read()
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()