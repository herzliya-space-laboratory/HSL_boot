import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from datetime import datetime
from TLE_cal import  get_passes, convert_passes_str

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)#import importlib
#importlib.import_module(os.path.abspath(os.getcwd()) + "/utility/TLE_cal.py")

logger = logging.getLogger(__name__)


def get_token_file():
    f_token = open("Telegram_token", "r")
    return f_token.read()


def echo(update, context):
    massage = "/get_passes - for getting top 5 passes\n"
    massage += "/get_place - get the cordinates of Duchifat 3 in a specific time\n"
    #massage += "/get_place - get the cordinates of Duchifat 3 in a specific time\n"
    update.message.reply_text(massage)

def get_passes_me(update, context):
    #passes = "Return sometime later... Remember I am always here for you"
    passes = get_passes([32.1624, 34.8447], 19.2080, "DUCHIFAT-3", datetime.utcnow(), 24, 5)
    passes = convert_passes_str(passes)
    string = ""
    for pass_ in passes:
        for item in pass_:
            string += str(item) + ", "
        string += "\n"
    update.message.reply_text(string)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    updater = Updater(get_token_file(), use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("get_passes", get_passes_me))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()