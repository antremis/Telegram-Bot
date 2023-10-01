import os
import telebot
from dotenv import load_dotenv
from PIL import ImageGrab
import io
import pytesseract
load_dotenv()

API_TOKEN = os.getenv('TELEGRAM_BOT_API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['test'])
def test(message):
    bot.send_message(message.chat.id, "I am working!")

@bot.message_handler(commands=['ss'])
def greet(message):
    screenshot = ImageGrab.grab()
    
    # Convert the screenshot to a byte stream
    screenshot_bytes = io.BytesIO()
    screenshot.save(screenshot_bytes, format='PNG')
    screenshot_bytes.seek(0)
    
    # Send the screenshot to the user
    bot.send_photo(chat_id=message.chat.id, photo=screenshot_bytes)

@bot.message_handler(commands=['ocr'])
def greet(message):
    screenshot = ImageGrab.grab()
    text = pytesseract.image_to_string(screenshot)
    
    # Convert the screenshot to a byte stream
    screenshot_bytes = io.BytesIO()
    screenshot.save(screenshot_bytes, format='PNG')
    screenshot_bytes.seek(0)
    
    # Send the screenshot to the user
    bot.send_photo(chat_id=message.chat.id, photo=screenshot_bytes)
    bot.send_message(message.chat.id, text)

if __name__ == '__main__':
    bot.polling()