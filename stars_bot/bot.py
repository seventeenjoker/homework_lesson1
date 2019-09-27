from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem
from datetime import date 

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    user_text = 'Hello stranger! Here you can get information about Planet in constellation on today. ' \
                'Tell me now which planet you wanna know about? Use /planet planet_name ;)'
    update.message.reply_text(user_text)

def check_the_sign(bot, update):
    text = 'Вызвана /planet'
    logging.info(text)
    today = date.today().strftime("%Y/%m/%d")
    planets_dic = {
        'Mars': ephem.Mars,
        'Moon': ephem.Moon,
        'Saturn': ephem.Saturn,
        'Jupiter': ephem.Jupiter,
        'Uranus': ephem.Uranus,
        'Neptune': ephem.Neptune,
        'Pluto': ephem.Pluto,
        'Sun': ephem.Sun,
        'Venus': ephem.Venus
    }
    message = update.message.text
    command, planet = message.split()
    planet_new = planet.capitalize()
    pl = planets_dic.get(planet_new, 0)
    misunderstanding = "I didn't get you, sorry. Try '/planet sun'"
    # error_message = 'Ooops...something went wrong...'
    if pl:
        update.message.reply_text(ephem.constellation(pl(today)))
    else:
        update.message.reply_text(misunderstanding)

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    logging.info('Бот запускается.')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', check_the_sign))
    # dp.add_handler(CommandHandler(Filters.text, check_the_sign))

    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()