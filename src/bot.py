import telebot
from telebot.types import Message
from kandinsky import generate_img
from telebot import types
from dependencies import TELEGRAM_BOT_API
from telebot import types

bot = telebot.TeleBot(TELEGRAM_BOT_API)


# Handle '/start' and '/help'
@bot.message_handler(commands=["help", "start"])
def send_welcome(message):
    bot.reply_to(
        message,
        text='Для того, чтобы сгенерировать изображение, отправьте в следующем сообщении ключевые слова через запятую.'.format(
            message.from_user
        ),
    )


# set prompt
@bot.message_handler(content_types=["text"])
def func(message: Message):
    """
    Main action function
    :param message: telebot.types.Message
    :return:
    """
    new_message = bot.send_message(chat_id=message.chat.id, text='Идет генерация изображения...')
    text_prompt: str = message.text
    generated_image = generate_img(text_prompt)
    bot.delete_message(chat_id=new_message.chat.id, message_id=new_message.message_id)
    bot.send_photo(chat_id=message.chat.id, photo=generated_image[0])


if __name__ == '__main__':
    bot.infinity_polling(timeout=99999, skip_pending=True)
