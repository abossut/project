from airogram import Bot, Dispatcher, executor, types
from airogram.types.web_app_info import WebAppInfo

bot = telebot.TeleBot("6885562987:AAEtcpcfvlOX9Vj_3yPRCJ81NsSuNaGK-Gk")
dp = Dispatcher(bot)


dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('открыть веб страницу', web_app=WebAppInfo(url='')))
    await message.answer('Привет!', reply_markup=markup)


executor.start_polling(dp)
