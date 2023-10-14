import re

import telebot
from telebot.types import Message

from dependencies import TELEGRAM_BOT_API
from kandinsky import generate_img

bot = telebot.TeleBot(TELEGRAM_BOT_API)

command_arguments = {
    "negative": r"(-n|—n|--neg|--negative|—neg|—negative)",
    "seed": r"(-s|--seed|—seed|—s)",
}


def clear_telegram_message(plain_text: str, arg_dict: dict[str, str]):
    main_message = plain_text

    for arg_field in arg_dict.values():
        arg_pattern = f"{arg_field}\s+([^\\s]+(\s+[^\\s]+)*)"
        main_message = re.sub(arg_pattern, "", main_message)

    # Remove leading/trailing whitespace from the main message
    main_message = main_message.strip()

    return main_message


def parse_telegram_args(plain_text: str, arg_dict: dict[str, str]):
    args = {}

    for arg_name, arg_field in arg_dict.items():
        arg_pattern = f"{arg_field}\s+([^\\s]+(\s+[^\\s]+)*)"
        matches = re.findall(arg_pattern, plain_text)
        if matches:
            args[arg_name] = matches[-1][1]
            args[arg_name] = clear_telegram_message(args[arg_name], arg_dict)

    return args


# Handle '/start' and '/help'
@bot.message_handler(commands=["help", "start"])
def send_welcome(message):
    """
    Send welcome message
    :param message: telebot.types.Message
    :return:
    """
    bot.reply_to(
        message,
        text="Для того, чтобы сгенерировать изображение,"
        " отправьте в следующем сообщении ключевые слова через запятую.".format(
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
    main_message = clear_telegram_message(message.text, command_arguments)
    args = parse_telegram_args(message.text, command_arguments)

    new_message = bot.send_message(
        chat_id=message.chat.id, text="Идет генерация изображения..."
    )
    generated_image = generate_img(text_prompt=main_message, **args)

    bot.delete_message(chat_id=new_message.chat.id, message_id=new_message.message_id)
    bot.send_photo(chat_id=message.chat.id, photo=generated_image[0])


if __name__ == "__main__":
    bot.infinity_polling(timeout=99999, skip_pending=True)
