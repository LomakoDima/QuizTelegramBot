import telebot
from config import token
# Задание 7 - испортируй команду defaultdict
from collections import defaultdict
from logic import quiz_questions



user_responses = defaultdict(int)
# Задание 8 - создай словарь points для сохранения количества очков пользователя
points = defaultdict(int)

bot = telebot.TeleBot(token)


def send_question(chat_id):
    """Отправляет пользователю следующий вопрос или завершает викторину."""
    if user_responses[chat_id] < len(quiz_questions):
        question = quiz_questions[user_responses[chat_id]]
        bot.send_message(chat_id, f"\U0001F4A1 Вопрос {user_responses[chat_id] + 1}:\n{question.text}",
                         reply_markup=question.gen_markup())
    else:
        bot.send_message(chat_id, f"\U0001F3C6 Викторина завершена!\n\U0001F4B0 Ваш результат: {points[chat_id]} очков")


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    """Обрабатывает ответы пользователей."""
    chat_id = call.message.chat.id

    if call.data == "correct":
        points[chat_id] += 1
        bot.answer_callback_query(call.id, "\U0001F389 Ответ верный!\U0001F389")
    else:
        bot.answer_callback_query(call.id, "\U000026A0 Ответ неверный! Попробуйте снова.")

    user_responses[chat_id] += 1
    send_question(chat_id)


@bot.message_handler(commands=['start'])
def start(message):
    """Запускает викторину для нового пользователя."""
    chat_id = message.chat.id
    if chat_id not in user_responses:
        user_responses[chat_id] = 0
        points[chat_id] = 0
        bot.send_message(chat_id,
                         "\U0001F680 Добро пожаловать в викторину! Ответьте на вопросы и проверьте свои знания!\n\U0001F4DA Готовы? Тогда поехали!")
        send_question(chat_id)


# Запуск бота
bot.infinity_polling()

