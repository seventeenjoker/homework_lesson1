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
    user_text = 'Hello stranger! Here you can get information about Planet in constellation on today. Tell me now which planet you wanna know about? Use /planet planet_name ;)'
    update.message.reply_text(user_text)

def check_the_sign(bot, update):
    text = 'Вызвана /planet'
    logging.info(text)
    today = date.today().strftime("%Y/%m/%d")
    planets_dic = {
        'Mars': ephem.Mars,
        'Moon': ephem.Moon,
        'Saturn': ephem.Moon,
        'Jupiter': ephem.Jupiter,
        'Uranus': ephem.Uranus,
        'Neptune': ephem.Neptune,
        'Pluto': ephem.Pluto,
        'Sun': ephem.Sun,
        'Venus': ephem.Venus
    }
    message = update.message.text
    planet = message.split(' ')
    planet_new = planet[1].capitalize()
    print(planet_new)
    misunderstanding = "I didn't get you, sorry. Try '/planet sun'"
    error_message = 'Ooops...something went wrong...'
    if planet_new in planets_dic:
        update.message.reply_text(ephem.constellation(planets_dic[planet_new](today)))
    # try:
    #     if planet[1] == 'Mars':
    #         planet = ephem.Mars(today)
    #         update.message.reply_text(ephem.constellation(planet))
    #     elif planet[1] == 'Moon':
    #         planet = ephem.Moon(today)
    #         update.message.reply_text(ephem.constellation(planet))
    #     elif planet[1] == 'Saturn':
    #         planet = ephem.Moon(today)
    #         update.message.reply_text(ephem.constellation(planet))
    #     elif planet[1] == 'Jupiter':
    #         planet = ephem.Jupiter(today)
    #         update.message.reply_text(ephem.constellation(planet))
    #     elif planet[1] == 'Uranus':
    #         planet = ephem.Uranus(today)
    #         update.message.reply_text(ephem.constellation(planet))
    #     elif planet[1] == 'Neptune':
    #         planet = ephem.Neptune(today)
    #         update.message.reply_text(ephem.constellation(planet))
    #     elif planet[1] == 'Pluto':
    #         planet = ephem.Pluto(today)
    #         update.message.reply_text(ephem.constellation(planet))
    #     elif planet[1] == 'Sun':
    #         planet = ephem.Sun(today)
    #         update.message.reply_text(ephem.constellation(planet))
    #     else:
    #         update.message.reply_text(misunderstanding)
    # except:
    #     logging.info(error_message)

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    logging.info('Бот запускается.')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', check_the_sign))
    # dp.add_handler(CommandHandler(Filters.text, check_the_sign))

    mybot.start_polling()
    mybot.idle()

main()