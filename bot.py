import qrcode
import telebot
from telebot import types
import time

TOKEN = '5326812340:AAEubaelzkBO6FJj8zHTpdQTEOojd9XxS4g'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def command_help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('===CREATE QR-CODE===')

    markup.add(item1)

    bot.send_message(message.chat.id, "==============\nUSE BUTTONS\n==============", reply_markup=markup)



@bot.message_handler(content_types=['text'])
def create(message):
	if message.text == '===CREATE QR-CODE===':
		bot.send_message(message.chat.id, '<?/!PLEASE SEND ME WHAT YOU WANT TO SAVE IN THE QR-CODE!/?>')
		bot.send_message(message.chat.id, '<↓""LINK""↓>')
		bot.send_message(message.chat.id, '<↓""CONTACT""↓>')
		bot.send_message(message.chat.id, '<↓""PHOTO URL""↓>')
		bot.send_message(message.chat.id, '<↓""TEXT IN ENGLISH""↓>')

	elif message.text == message.text:
		img = qrcode.make(message.text)

		type(img)
		img.save(message.text + ".png")
		
		bot.send_message(message.chat.id, 'Success!')
		bot.send_message(message.chat.id, 'Please wait 3 seconds')
		
		time.sleep(3)
		photo = open(message.text + ".png", 'rb')
		bot.send_photo(message.chat.id, photo)


		

bot.infinity_polling()