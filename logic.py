import telebot
from config import token
from collections import defaultdict
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


bot = telebot.TeleBot(token)

# Словари для отслеживания ответов и очков пользователей
user_responses = defaultdict(int)
points = defaultdict(int)

class Question:
    def __init__(self, text, answer_id, *options):
        self.__text = text
        self.__answer_id = answer_id
        self.options = options

    @property
    def text(self):
        return self.__text

    def gen_markup(self):
        markup = InlineKeyboardMarkup()
        for i, option in enumerate(self.options):
            callback_data = "correct" if i == self.__answer_id else "wrong"
            markup.add(InlineKeyboardButton(option, callback_data=callback_data))
        return markup

# Список вопросов
quiz_questions = [
    Question("\U0001F30D Что из этого не является планетой?", 1, "\U0001F30F Венера", "\U0001F311 Луна", "\U0001F30D Сатурн", "\U0001F319 Марс"),
    Question("\U0001F431 Как котики выражают свою любовь?", 0, "\U0001F496 Громким мурлыканием", "\U0001F4F7 Отправляют фото на Instagram", "\U0001F436 Гавкают"),
    Question("\U0001F4DA Какие книги котики любят читать?", 3, "\U0001F431 Обретение вашего внутреннего урр-мирения", "\U000023F3 Тайм-менеджмент или как выделить 18 часов в день для сна", "\U0001F4A4 101 способ уснуть на 5 минут раньше, чем хозяин", "\U0001F4D6 Пособие по управлению людьми")
]