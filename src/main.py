import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

# Приветственное сообщение при команде '/start'


@bot.message_handler(commands=['start'])
def zdarova(message):
    bot.send_message(message.chat.id, "Жеееесть, {0.first_name} опять жрать хочет".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)


# Клавиатура
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton('Чё сожрать?')

markup.add(item1)

# Кароч делаем так: думаем, как часто можна жрать каждый вид еды,
# и берем количество дней в месяце, в которые этот вид еды будет жраться
# (всего в сесяце пусть будет 28 дней, иначе че-то криво получается).
# Спитон дальши сам разберется, кому че вставить в жопу
жри = [
  {'food': 'Сожри пицц',                'weight': 2 },    # 2 в сесяц
  {'food': 'Сожри роллс',               'weight': 1 },    # 1 в сесяц
  {'food': 'Сожри курицу из KFC',       'weight': 8 },    # 2 раза в неделю
  {'food': 'Сожри чикан',               'weight': 0 },    # 0 раз (только с сырной коллеццией можна жрать это, в последний сас была зимой)
  {'food': 'Сожри арбыс или дыню',      'weight': 1 },    # 1 раз в сесяц
  {'food': 'Сожри бургерс' ,            'weight': 8 },    # 1 раз в неделю
  {'food': 'Сожри шашлык',              'weight': 4 },    # 1 раз в неделю
  {'food': 'Сожри шаурму',              'weight': 4 },    # 1 раз в неделю
  {'food': 'Сожри хинкали с хачапури',  'weight': 1 },    # 1 раз в месяц
  {'food': 'Сожри сэсвич',              'weight': 2 },    # 2 раза в сесяц (осталось найти где их жрать)
  {'food': 'Сожри стейк',               'weight': 1 },    # 1 раз в сесяц
  {'food': 'Сожри блин',                'weight': 2 },    # 2 раза в сесяц
  {'food': 'Сожри пак гадюки',          'weight': 1 },    # 1 раз в сесяц
  {'food': 'Сожри ночной снэк',         'weight': 8 },    # 2 раза в неделю
  {'food': 'Сожри рамен',               'weight': 4 },    # 1 раз в неделю
  {'food': 'Сожри WOK',                 'weight': 4 },    # 1 раз в неделю
  {'food': 'Сожри рыс с яйцом',         'weight': 4 },    # 1 раз в неделю
  {'food': 'Сожри сало',                'weight': 2 },    # 2 раза в сесяц
  {'food': 'Сожри CUMнам',              'weight': 1 },    # 1 раз в сесяц
  {'food': 'Сожри чабуреки',            'weight': 2 },    # 2 раза в сесяц
  {'food': 'Сожри пироженку',           'weight': 1 },    # 1 раз в сесяц
  {'food': 'Сожри колбаски',            'weight': 2 },    # 2 раза в сесяц
  {'food': 'Сожри понтовые вафли',      'weight': 1 },    # 1 раз в сесяц
  {'food': 'Сожри карбонару',           'weight': 2 },    # 2 раза в сесяц
  {'food': 'Сожри торт',                'weight': 1 },    # 1 раз в сесяц
]

foods = list(map(lambda x: x['food'], жри))
weights = list(map(lambda x: x['weight'], жри))


@bot.message_handler(content_types=['text'])
def messagelist(message):
  if message.text == 'Чё сожрать?':
    bot.send_message(message.chat.id, random.choices(population=foods, weights=weights, k=1)[0])
  else:
    bot.send_message(message.chat.id, 'Блять, ты тупой? Тут одна кнопка, на неё и жми жесть')


# Запуск бота
bot.polling(none_stop=True, interval=0)
