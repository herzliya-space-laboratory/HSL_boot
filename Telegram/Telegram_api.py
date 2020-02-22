import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep
from utility.TLE_cal import get_location_time


def get_token_file():
    f_token = open("Telegram/Telegram_token", "r")
    return f_token.read()
