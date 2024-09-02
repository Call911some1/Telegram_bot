# 1 Импорт библиотек
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message #лови все оновления этого типа
from aiogram.filters.command import Command #обработка команд /start, /help и другие

#2 Инициализация объектов
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO, filename='bot.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#3 Обработка команды /start 
@dp.message(Command(commands=['start']))
async def proccess_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Чтобы поменять имя с кириллицы на латиницу, просто введите сюда ваше имя'
    logging.info(f"{user_name} {user_id} запустил бота")
    await bot.send_message(chat_id=user_id, text=text)

#4 Обработка всех сообщений
table = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "e", 
    "ж": "zh", "з": "z", "и": "i", "й": "i", "к": "k", "л": "l", "м": "m", 
    "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u", 
    "ф": "f", "х": "kh", "ц": "ts", "ч": "ch", "ш": "sh", "щ": "shch", 
    "ъ": "ie", "ы": "y", "ь": "", "э": "e", "ю": "iu", "я": "ia"
}
@dp.message()
async def ru_eng_name_converter(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text.lower()
    list_full_name = text.split()
    list_result = []

    for word in list_full_name:
        converted_word = ""

        for char in word:
            converted_char = table.get(char, char)
            converted_word += converted_char
        
        final_word = converted_word.capitalize()
        list_result.append(final_word)

    logging.info(f"{user_name} {user_id}: {text} ")
    await message.answer(" ".join(list_result))

#5 Запуск процесса пуллинга
if __name__ == '__main__':
    dp.run_polling(bot)