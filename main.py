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
    questation = quiz_questions[user_responses[chat_id]]
    bot.send_message(chat_id, questation.text, reply_markup=questation.gen_markup())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):

    if call.data == "correct":
        bot.answer_callback_query(call.id, "Answer is correct")
        # Задание 9 - добавь очки пользователю за правильный ответ
        points[call.message.chat.id] = points.get(call.message.chat.id, 0) + 1
    elif call.data == "wrong":
        bot.answer_callback_query(call.id,  "Answer is wrong")
      
    # Задание 5 - реализуй счетчик вопросов
    user_responses[call.message.chat.id] += 1



    # Задание 6 - отправь пользователю сообщение с количеством его набранных очков, если он ответил на все вопросы, а иначе отправь следующий вопрос
    def callback_query(call):
        chat_id = call.message.chat.id

        if call.data == "correct":
            points[chat_id] += 1
            bot.answer_callback_query(call.id, "Answer is correct")
        else:
            bot.answer_callback_query(call.id, "Answer is wrong")

        if user_responses[chat_id] < len(quiz_questions):
            send_question(chat_id)
        else:
            bot.send_message(chat_id, f"Ваш результат: {points[chat_id]}")


@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id not in user_responses.keys():
        user_responses[message.chat.id] = 0
        send_question(message.chat.id)


bot.infinity_polling()
