# Задание 2 - Импортируй нужные классы
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

class Question:

    def __init__(self, text, answer_id, *options):
        self.__text = text
        self.__answer_id = answer_id
        self.options = options

    # Задание 1 - Создай геттер для получения текста вопроса
    @property
    def text(self):
        return self.__text

    

        # Задание 3 - Создай метод для генерации Inline клавиатуры
    def gen_markup(self):
        markup = InlineKeyboardMarkup()
        for i, option in enumerate(self.options):
            callback_data = "correct" if i == self.__answer_id else "wrong"
            markup.add(InlineKeyboardButton(option, callback_data=callback_data))
        return markup



# Задание 4 - заполни список своими вопросами
quiz_questions = [
    Question("Что из этого не является планетой?", 1, "Венера", "Луна", "Сатурн", "Марс"),
    Question("Как котики выражают свою любовь?", 0, "Громким мурлыканием", "Отправляют фото на Instagram", "Гавкают"),
    Question("Какие книги котики любят читать?", 3, "Обретение вашего внутреннего урр-мирения", "Тайм-менеджмент или как выделить 18 часов в день для сна", "101 способ уснуть на 5 минут раньше, чем хозяин", "Пособие по управлению людьми")
]

