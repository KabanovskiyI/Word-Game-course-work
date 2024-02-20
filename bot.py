import telebot
import emoji
import logics
from telebot import types

bot = telebot.TeleBot('6451674061:AAEo0cmwRdSiV0wp2DF0v4ZzSYTI2_L0xQc')
database = ''
theme = ''
input_list = []

@bot.message_handler(commands = ['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    rules = types.KeyboardButton('Правила гри' + emoji.emojize('📜'))
    start = types.KeyboardButton('Почати' + emoji.emojize('⚔'))
    markup.add(rules, start)
    
    bot.send_message(message.chat.id, 'Привіт! Це бот з яким ти можешь грати в слова!\nПравила гри: перший гравець називає слово, а другий повинен запропонувати інше, що починається з тієї букви, на яку закінчується назване.', reply_markup = markup)

@bot.message_handler(func = lambda message: message.text == 'Правила гри' + emoji.emojize('📜'))
def rules_game(message):
    bot.send_message(message.chat.id, 'Перший гравець називає слово, а другий повинен запропонувати інше, що починається з тієї букви, на яку закінчується назване.')


@bot.message_handler(func = lambda message: message.text == 'Почати' + emoji.emojize('⚔'))
def Choice_theme_game(message):

    global database
    database = ''

    keyboard_choice = types.ReplyKeyboardMarkup(resize_keyboard=True)

    rules = types.KeyboardButton('Правила гри' + emoji.emojize('📜'))
    theme_country = types.KeyboardButton('Країни' + emoji.emojize('🌏'))
    theme_city = types.KeyboardButton('Міста' + emoji.emojize('🏘'))
    theme_animals = types.KeyboardButton('Тварини' + emoji.emojize('🦥'))
    theme_plants = types.KeyboardButton('Рослини' + emoji.emojize('🍀'))
    theme_food = types.KeyboardButton('Страви' + emoji.emojize('🍔'))

    keyboard_choice.add(rules).row(theme_country, theme_city, theme_animals, theme_plants, theme_food)

    bot.send_message(message.chat.id, 'Обери тему', reply_markup = keyboard_choice)

def themes_button(message):
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    rules = types.KeyboardButton('Правила гри' + emoji.emojize('📜'))
    main_menu = types.KeyboardButton('Головне меню' + emoji.emojize('🔍'))
    menu.add(rules, main_menu)
    bot.send_message(message.chat.id, 'Введіть своє слово' + emoji.emojize('📝'), reply_markup = menu)

@bot.message_handler(func = lambda message: message.text == 'Країни' + emoji.emojize('🌏'))
def open_country(message):
    themes_button(message)
    global database
    global theme

    theme = 'Country'
    database = 'Data\Country.txt'

@bot.message_handler(func = lambda message: message.text == 'Міста' + emoji.emojize('🏘'))
def open_city(message):
    themes_button(message)
    global database
    global theme

    theme = 'City'
    database = 'Data\City.txt'

@bot.message_handler(func = lambda message: message.text == 'Тварини' + emoji.emojize('🦥'))
def open_animals(message):
    themes_button(message)
    global database
    global theme

    theme = 'Animals'
    database = 'Data\Animals.txt'

@bot.message_handler(func = lambda message: message.text == 'Рослини' + emoji.emojize('🍀'))
def open_plants(message):
    themes_button(message)
    global database
    global theme

    theme = 'Plants'
    database = 'Data\Plants.txt'

@bot.message_handler(func = lambda message: message.text == 'Страви' + emoji.emojize('🍔'))
def open_food(message):
    themes_button(message)
    global database
    global theme

    theme = 'Food'
    database = 'Data\Food.txt'

@bot.message_handler(func = lambda message: message.text == 'Головне меню' + emoji.emojize('🔍'))
def start_main_menu(message):
    Choice_theme_game(message)


@bot.message_handler(commands = ['notfound'])
def yes_or_not(message):
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Yes = types.KeyboardButton(emoji.emojize('✅'))
    Not = types.KeyboardButton(emoji.emojize('❌'))
    menu.add(Yes, Not)
    bot.send_message(message.chat.id, 'Підтвердіть дію',reply_markup = menu)

@bot.message_handler(func = lambda message: message.text == emoji.emojize('✅'))
def recording(message):
    global input_list
    global database
    last_el = input_list[-1]
    logics.Search(last_el, database, theme).Recording(last_el, database)
    bot.send_message(message.chat.id, 'Слово додане в базу даних' + emoji.emojize('📝'))
    themes_button(message)

@bot.message_handler(func = lambda message: message.text == emoji.emojize('❌'))
def not_recording(message):
    themes_button(message)


@bot.message_handler(func = lambda message: True)
def get_user_word(message):
    
    global database
    global input_list
    global theme

    input_word = message.text.strip()
    
    if database == '':
        bot.send_message(message.chat.id, 'Оберіть одну з наданих дій')
    else:
        result = logics.Search(input_word, database, theme).Search()
        bot.send_message(message.chat.id, result)
        input_list.append(input_word)

bot.polling(none_stop = True)