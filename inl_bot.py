import telebot
from telebot import types


bot = telebot.TeleBot('859963415:AAFJ3Y6fMG2_V76hoL1ZeeG65sWioKLWBOo')


@bot.message_handler(commands=["start"])
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Русский", callback_data="rus")
    keyboard.add(callback_button)
    callback_button_1 = types.InlineKeyboardButton(text="Казахский", callback_data="kz")
    keyboard.add(callback_button_1)
    bot.send_message(message.chat.id, "Выберите язык общения", reply_markup = keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'rus')
def callback_inline_lvl1(call):
    markup = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Наши услуги", callback_data="ysl")
    markup.add(callback_button)
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "rus":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вас приветствует Super Ломбард", reply_markup = markup)

@bot.callback_query_handler(func=lambda call: call.data == 'ysl')
def callback_inline_lvl1(call):
    markup = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Золото ломбард", callback_data="gold")
    markup.add(callback_button)
    callback_button_1 = types.InlineKeyboardButton(text="Авто ломбард", callback_data="auto")
    markup.add(callback_button_1)
    callback_button_2 = types.InlineKeyboardButton(text="Техно ломбард", callback_data="techno")
    markup.add(callback_button_2)
    callback_button_3 = types.InlineKeyboardButton(text="Рефинансирование", callback_data="refin")
    markup.add(callback_button_3)
    callback_button_4 = types.InlineKeyboardButton(text="Продажа золота", callback_data="sale_gold")
    markup.add(callback_button_4)
    callback_button_5 = types.InlineKeyboardButton(text="Продажа техники и норковых шуб", callback_data="sale_norki")
    markup.add(callback_button_5)
    callback_button_6 = types.InlineKeyboardButton(text="Наши филиалы", callback_data="fil")
    markup.add(callback_button_6)
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "ysl":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Super Ломбард", reply_markup = markup)

@bot.callback_query_handler(func=lambda call: call.data == 'gold')
def callback_inline_lvl2(call):
    markup = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Предметы залога", callback_data="things")
    markup.add(callback_button)
    callback_button_1 = types.InlineKeyboardButton(text="Филиалы", callback_data="branch")
    markup.add(callback_button_1)
    callback_button_2 = types.InlineKeyboardButton(text="Онлайн расчет", callback_data="online_trans")
    markup.add(callback_button_2)
    callback_button_3 = types.InlineKeyboardButton(text="Консультация", callback_data="cons")
    markup.add(callback_button_3)
    callback_button_4 = types.InlineKeyboardButton(text="Права клиента", callback_data="rights")
    markup.add(callback_button_4)
    callback_button_5 = types.InlineKeyboardButton(text="Условия", callback_data="conditionals")
    markup.add(callback_button_5)
    callback_button_6 = types.InlineKeyboardButton(text="Вернуться в главное меню", callback_data="main_back")
    markup.add(callback_button_6)
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "gold":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вас приветствует «Super Ломбард»", reply_markup = markup)

@bot.callback_query_handler(func=lambda call: call.data == 'auto')
def callback_inline_lvl4(call):
    markup = types.InlineKeyboardMarkup()
    call_back_button = types.InlineKeyboardButton(text="Предметы залога", callback_data= "things_auto")
    call_back_button_1 = types.InlineKeyboardButton(text="Филиал", callback_data="filial_auto")
    call_back_button_2 = types.InlineKeyboardButton(text="Страхование", callback_data="strakh_auto")
    call_back_button_3 = types.InlineKeyboardButton(text="Консультация", callback_data="kons_auto")
    call_back_button_4 = types.InlineKeyboardButton(text="Условия", callback_data="ysl_auto")
    call_back_button_5 = types.InlineKeyboardButton(text="Вернуться в главное меню", callback_data="main_back")
    markup.add(call_back_button)
    markup.add(call_back_button_1)
    markup.add(call_back_button_2)
    markup.add(call_back_button_3)
    markup.add(call_back_button_4)
    markup.add(call_back_button_5)
    if call.message:
        if call.data == "auto":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вас приветствует «Super Ломбард»", reply_markup = markup)

@bot.callback_query_handler(func=lambda call: call.data == 'techno')
def callback_inline_lvl5(call):
    markup = types.InlineKeyboardMarkup()
    call_back_button = types.InlineKeyboardButton(text="Предметы залога", callback_data= "things_techno")
    call_back_button_1 = types.InlineKeyboardButton(text="Филиалы", callback_data="filial_techno")
    call_back_button_2 = types.InlineKeyboardButton(text="Консультация", callback_data="kons_techno")
    call_back_button_3 = types.InlineKeyboardButton(text="Условия", callback_data="ysl_techno")
    callback_back = types.InlineKeyboardButton(text="Вернуться в предыдущее меню", callback_data="main_back")
    markup.add(call_back_button)
    markup.add(call_back_button_1)
    markup.add(call_back_button_2)
    markup.add(call_back_button_3)
    markup.add(callback_back)
    if call.message:
        if call.data == "techno":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вас приветствует «Super Ломбард»", reply_markup = markup)

@bot.callback_query_handler(func=lambda call: call.data == 'refin')
def callback_inline_lvl6(call):
    markup = types.InlineKeyboardMarkup()
    call_back_button = types.InlineKeyboardButton(text="Консультация", callback_data= "kons_refin")
    callback_back = types.InlineKeyboardButton(text="Вернуться в предыдущее меню", callback_data="main_back")
    markup.add(call_back_button)
    markup.add(callback_back)
    if call.message:
        if call.data == "refin":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вас приветствует «Super Ломбард»", reply_markup = markup)

@bot.callback_query_handler(func=lambda call: call.data == 'sale_gold')
def callback_inline_lvl7(call):
    markup = types.InlineKeyboardMarkup()
    call_back_button = types.InlineKeyboardButton(text="Филиалы", callback_data="filial_sale_gold")
    call_back_button_1 = types.InlineKeyboardButton(text="Инстаграмм", callback_data="inst_sale_gold")
    call_back_button_2 = types.InlineKeyboardButton(text="Консультация", callback_data= "kons_sale_gold")
    markup.add(call_back_button)
    markup.add(call_back_button_1)
    markup.add(call_back_button_2)
    if call.message:
        if call.data == "sale_gold":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вас приветствует «Super Ломбард»", reply_markup = markup)

@bot.callback_query_handler(func=lambda call: call.data == 'sale_norki')
def callback_inline_lvl8(call):
    markup = types.InlineKeyboardMarkup()
    call_back_button = types.InlineKeyboardButton(text="Филиалы", callback_data="filial_sale_norki")
    call_back_button_1 = types.InlineKeyboardButton(text="Инстаграмм", callback_data="inst_sale_norki")
    callback_back = types.InlineKeyboardButton(text="Вернуться в предыдущее меню", callback_data="main_back")
    markup.add(call_back_button)
    markup.add(call_back_button_1)
    markup.add(callback_back)
    if call.message:
        if call.data == "sale_norki":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вас приветствует «Super Ломбард»", reply_markup = markup)


@bot.callback_query_handler(func=lambda call: call.data == 'fil')
def callback_inline_lvl9(call):
    markup = types.InlineKeyboardMarkup()
    call_back_button = types.InlineKeyboardButton(text="Адреса и контакты", callback_data="fil_adress")
    call_back_button_1 = types.InlineKeyboardButton(text="Условия", callback_data="fil_ysl")
    callback_back = types.InlineKeyboardButton(text="Вернуться в предыдущее меню", callback_data="main_back")
    markup.add(call_back_button)
    markup.add(call_back_button_1)
    markup.add(callback_back)
    if call.message:
        if call.data == "fil":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вас приветствует «Super Ломбард»", reply_markup = markup)

@bot.callback_query_handler(func=lambda call: call.data == 'things')
def callback_inline_lvl3(call):
    markup = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Вернуться в предыдущее меню", callback_data="back")
    markup.add(callback_button)
    if call.message:
        if call.data == "things":
            bot.send_message(call.message.chat.id, text = "Золото\n Лом из сплава золота\n Бриллианты", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'back')
def callback_inline_lvl45(call):
    if call.message:
        if call.data == "back":
            back_keyboard = types.InlineKeyboardMarkup()
            back_call_back_button = types.InlineKeyboardButton(text="Предметы залога", callback_data="things_auto")
            back_call_back_button_1 = types.InlineKeyboardButton(text="Филиал", callback_data="filial_auto")
            back_call_back_button_2 = types.InlineKeyboardButton(text="Страхование", callback_data="strakh_auto")
            back_call_back_button_3 = types.InlineKeyboardButton(text="Консультация", callback_data="kons_auto")
            back_call_back_button_4 = types.InlineKeyboardButton(text="Условия", callback_data="ysl_auto")
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text, reply_markup=back_keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'main_back')
def callback_inline_lvl46(call):
    markup = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Золото ломбард", callback_data="gold")
    markup.add(callback_button)
    callback_button_1 = types.InlineKeyboardButton(text="Авто ломбард", callback_data="auto")
    markup.add(callback_button_1)
    callback_button_2 = types.InlineKeyboardButton(text="Техно ломбард", callback_data="techno")
    markup.add(callback_button_2)
    callback_button_3 = types.InlineKeyboardButton(text="Рефинансирование", callback_data="refin")
    markup.add(callback_button_3)
    callback_button_4 = types.InlineKeyboardButton(text="продажа золота", callback_data="sale_gold")
    markup.add(callback_button_4)
    callback_button_5 = types.InlineKeyboardButton(text="Продажа техники и норковых шуб", callback_data="sale_norki")
    markup.add(callback_button_5)
    callback_button_6 = types.InlineKeyboardButton(text="Наши филиалы", callback_data="fil")
    markup.add(callback_button_6)
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "main_back":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text, reply_markup = markup)

@bot.callback_query_handler(func=lambda call: call.data == 'branch')
def callback_inline_lvl10(call):
    markup = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Вернуться в предыдущее меню", callback_data="back")
    markup.add(callback_button)
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "branch":
            bot.send_message(call.message.chat.id, text = "E-Mail: s-super111@mail.ru\n тел: 8 (7162) 72-27-20\n Автоломбард, г. Кокшетау: +7 702 921 48 61\n Автоломбард, г. Астана: +7 778 001 72 52\n Головной офис: г.Кокшетау, ул.Пушкина 14", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'online_trans')
def callback_inline_lvl11(call):
    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='Наш сайт', url='http://superlombard.kz')
    callback_button = types.InlineKeyboardButton(text="Вернуться в предыдущее меню", callback_data="back")
    markup.add(btn_my_site)
    markup.add(callback_button)
    if call.message:
        if call.data == "online_trans":
            bot.send_message(call.message.chat.id, "Нажмите на кнопку и перейди на наш сайт",
                             reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'cons')
def callback_inline_lvl12(call):
    markup = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Контакты", callback_data="cont_cons")
    callback_button_1 = types.InlineKeyboardButton(text="Вернуться в предыдущее меню", callback_data="back")
    markup.add(callback_button)
    markup.add(callback_button_1)
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "cons":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вас приветствует «Super Ломбард»", reply_markup = markup)

@bot.callback_query_handler(func=lambda call: call.data == 'cont_cons')
def callback_inline_lvl35(call):
    markup = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Вернуться в предыдущее меню", callback_data="back")
    markup.add(callback_button)
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "cont_cons":
            bot.send_message(call.message.chat.id, text = "E-Mail: s-super111@mail.ru\n тел: 8 (7162) 72-27-20\n Автоломбард, г. Кокшетау: +7 702 921 48 61\n Автоломбард, г. Астана: +7 778 001 72 52\n Головной офис: г.Кокшетау, ул.Пушкина 14",reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'rights')
def callback_inline_lvl13(call):
    markup = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Перерасчет процентов", callback_data="recalc")
    markup.add(callback_button)
    callback_button_1 = types.InlineKeyboardButton(text="Доверенное лицо (с 18 лет)", callback_data="trusted_face")
    markup.add(callback_button_1)
    callback_button_2 = types.InlineKeyboardButton(text="Частичный выкуп", callback_data="part_sale")
    markup.add(callback_button_2)
    callback_button_3 = types.InlineKeyboardButton(text="Продление", callback_data="prolong")
    callback_back = types.InlineKeyboardButton(text="Вернуться в предыдущее меню", callback_data="back")
    markup.add(callback_button_3)
    markup.add(callback_back)
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "rights":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вас приветствует «Super Ломбард»", reply_markup = markup)

@bot.callback_query_handler(func=lambda call: call.data == 'conditionals')
def callback_inline_lvl14(call):
    markup = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Вернуться в предыдущее меню", callback_data="back")
    markup.add(callback_button)
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "conditionals":
            bot.send_message(call.message.chat.id, text = "с 18 лет, при предъявлении документа удостоверяющий личность\n залог на 30 дней \n 0,2% за каждый день\n 0,4% пеня за каждый день\n", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'things_auto')
def callback_inline_lvl15(call):
    markup = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Автотранспортные средства", callback_data="auto_trans")
    callback_back = types.InlineKeyboardButton(text="Вернуться в предыдущее меню", callback_data="back")
    markup.add(callback_button)
    markup.add(callback_back)
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "things_auto":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вас приветствует «Super Ломбард»", reply_markup = markup)

@bot.callback_query_handler(func=lambda call: call.data == 'filial_auto')
def callback_inline_lvl16(call):
    markup = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Карта", callback_data="map_filial_auto")
    callback_back = types.InlineKeyboardButton(text="Вернуться в предыдущее меню", callback_data="back")
    markup.add(callback_button)
    markup.add(callback_back)
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "filial_auto":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вас приветствует «Super Ломбард»", reply_markup = markup)

@bot.callback_query_handler(func=lambda call: call.data == 'strakh_auto')
def callback_inline_lvl17(call):
    markup = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Контакты", callback_data="cont_filial_auto")
    callback_back = types.InlineKeyboardButton(text="Вернуться в предыдущее меню", callback_data="back")
    markup.add(callback_button)
    markup.add(callback_back)
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "strakh_auto":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вас приветствует «Super Ломбард»", reply_markup = markup)

@bot.callback_query_handler(func=lambda call: call.data == 'kons_auto')
def callback_inline_lvl18(call):
    markup = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Контакты", callback_data="cont_filial_auto")
    callback_back = types.InlineKeyboardButton(text="Вернуться в предыдущее меню", callback_data="back")
    markup.add(callback_button)
    markup.add(callback_back)
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "kons_auto":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вас приветствует «Super Ломбард»", reply_markup = markup)

@bot.callback_query_handler(func=lambda call: call.data == 'ysl_auto')
def callback_inline_lvl19(call):
    markup = types.InlineKeyboardMarkup()
    callback_back = types.InlineKeyboardButton(text="Вернуться в предыдущее меню", callback_data="back")
    markup.add(callback_back)
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "ysl_auto":
            bot.send_message(call.message.chat.id, text = "с 18 лет, при предъявлении документа удостоверяющий личность\n залог на 30 дней \n 0,2% за каждый день\n 0,4% пеня за каждый день\n")

@bot.callback_query_handler(func=lambda call: call.data == 'things_techno')
def callback_inline_lvl20(call):
    markup = types.InlineKeyboardMarkup()
    callback_back = types.InlineKeyboardButton(text="Вернуться в предыдущее меню", callback_data="back")
    markup.add(callback_back)
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "things_techno":
            bot.send_message(call.message.chat.id, text = " Телефоны\n Ноутбуки\n Телевизоры\n Бытовая техника (новая)\n")

@bot.callback_query_handler(func=lambda call: call.data == 'filial_techno')
def callback_inline_lvl21(call):
    markup = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Карта", callback_data="filial_techno")
    callback_back = types.InlineKeyboardButton(text="Вернуться в предыдущее меню", callback_data="back")
    markup.add(callback_button)
    markup.add(callback_back)
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "filial_techno":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вас приветствует «Super Ломбард»", reply_markup = markup)

@bot.callback_query_handler(func=lambda call: call.data == 'kons_techno')
def callback_inline_lvl22(call):
    markup = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Контакты", callback_data="cont_filial_techno")
    markup.add(callback_button)
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "kons_techno":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вас приветствует «Super Ломбард»", reply_markup = markup)

@bot.callback_query_handler(func=lambda call: call.data == 'ysl_techno')
def callback_inline_lvl23(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "ysl_techno":
            bot.send_message(call.message.chat.id, text = "с 18 лет, при предъявлении документа удостоверяющий личность\n залог на 30 дней \n 0,2% за каждый день\n 0,4% пеня за каждый день\n")

@bot.callback_query_handler(func=lambda call: call.data == 'kons_refin')
def callback_inline_lvl24(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "kons_refin":
            bot.send_message(call.message.chat.id, text = "Кокшетау ул. Абая 116, стадион «Окжетпес», 33 45 57\n Кокшетау ул. Абая 116,стадион «Окжетпес», 33 45 57\n Кокшетау ул. Абая 175, магазин Экспресс, 31 93 50\n Кокшетау ул. Гагарина 49,ТД Империал, 25 07 66\n Кокшетау пр.Аблай-Хана 30-31,возле маг. «Жаксы», 42 43 08\n Кокшетау мкрн. Боровской 53,маг. Тамерлан, 33 32 17\n Кокшетау пр. Нурсултана Назарбаева 64, 33 49 01\n Кокшетау ул. Достык 22, ТД Темирлан, 33 05 79\n Кокшетау ул. Мактая Сагдиева 48, 51 18 59\n Астана п-т Богенбай батыра 31, вп/1, 87076316509\n Астана ул. Петрова 23, 36-42-19\n Астана ул. Желтоксана 32, 32-85-90\n  Астана ул. Иле 30, маг. Тандем,29-97-83\n Астана ул. 189, маг. Даулет, 87072017340\n Алматы ул. Шолохова 4\n Алматы с.Туздыбастау ул. Алдабергенова 15\n")

@bot.callback_query_handler(func=lambda call: call.data == 'fil_sale_gold')
def callback_inline_lvl25(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "fil_sale_gold":
            bot.send_message(call.message.chat.id, text = "Кокшетау ул. Абая 116, стадион «Окжетпес», 33 45 57\n Кокшетау ул. Абая 116,стадион «Окжетпес», 33 45 57\n Кокшетау ул. Абая 175, магазин Экспресс, 31 93 50\n Кокшетау ул. Гагарина 49,ТД Империал, 25 07 66\n Кокшетау пр.Аблай-Хана 30-31,возле маг. «Жаксы», 42 43 08\n Кокшетау мкрн. Боровской 53,маг. Тамерлан, 33 32 17\n Кокшетау пр. Нурсултана Назарбаева 64, 33 49 01\n Кокшетау ул. Достык 22, ТД Темирлан, 33 05 79\n Кокшетау ул. Мактая Сагдиева 48, 51 18 59\n Астана п-т Богенбай батыра 31, вп/1, 87076316509\n Астана ул. Петрова 23, 36-42-19\n Астана ул. Желтоксана 32, 32-85-90\n  Астана ул. Иле 30, маг. Тандем,29-97-83\n Астана ул. 189, маг. Даулет, 87072017340\n Алматы ул. Шолохова 4\n Алматы с.Туздыбастау ул. Алдабергенова 15\n")

@bot.callback_query_handler(func=lambda call: call.data == 'inst_sale_gold')
def callback_inline_lvl26(call):
    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='Инстаграм', url='https://www.instagram.com/superlombard_astana/')
    markup.add(btn_my_site)
    if call.message:
        if call.data == "inst_sale_gold":
            bot.send_message(call.message.chat.id, "Нажмите на кнопку и перейди на наш профиль в инстаграм.",
                             reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'adress_kons_sale_gold')
def callback_inline_lvl27(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "adress_kons_sale_gold":
            bot.send_message(call.message.chat.id, text = "Кокшетау ул. Абая 116, стадион «Окжетпес», 33 45 57\n Кокшетау ул. Абая 116,стадион «Окжетпес», 33 45 57\n Кокшетау ул. Абая 175, магазин Экспресс, 31 93 50\n Кокшетау ул. Гагарина 49,ТД Империал, 25 07 66\n Кокшетау пр.Аблай-Хана 30-31,возле маг. «Жаксы», 42 43 08\n Кокшетау мкрн. Боровской 53,маг. Тамерлан, 33 32 17\n Кокшетау пр. Нурсултана Назарбаева 64, 33 49 01\n Кокшетау ул. Достык 22, ТД Темирлан, 33 05 79\n Кокшетау ул. Мактая Сагдиева 48, 51 18 59\n Астана п-т Богенбай батыра 31, вп/1, 87076316509\n Астана ул. Петрова 23, 36-42-19\n Астана ул. Желтоксана 32, 32-85-90\n  Астана ул. Иле 30, маг. Тандем,29-97-83\n Астана ул. 189, маг. Даулет, 87072017340\n Алматы ул. Шолохова 4\n Алматы с.Туздыбастау ул. Алдабергенова 15\n")

@bot.callback_query_handler(func=lambda call: call.data == 'filial_sale_norki')
def callback_inline_lvl28(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "filial_sale_norki":
            bot.send_message(call.message.chat.id, text = "Кокшетау ул. Абая 116, стадион «Окжетпес», 33 45 57\n Кокшетау ул. Абая 116,стадион «Окжетпес», 33 45 57\n Кокшетау ул. Абая 175, магазин Экспресс, 31 93 50\n Кокшетау ул. Гагарина 49,ТД Империал, 25 07 66\n Кокшетау пр.Аблай-Хана 30-31,возле маг. «Жаксы», 42 43 08\n Кокшетау мкрн. Боровской 53,маг. Тамерлан, 33 32 17\n Кокшетау пр. Нурсултана Назарбаева 64, 33 49 01\n Кокшетау ул. Достык 22, ТД Темирлан, 33 05 79\n Кокшетау ул. Мактая Сагдиева 48, 51 18 59\n Астана п-т Богенбай батыра 31, вп/1, 87076316509\n Астана ул. Петрова 23, 36-42-19\n Астана ул. Желтоксана 32, 32-85-90\n  Астана ул. Иле 30, маг. Тандем,29-97-83\n Астана ул. 189, маг. Даулет, 87072017340\n Алматы ул. Шолохова 4\n Алматы с.Туздыбастау ул. Алдабергенова 15\n")

@bot.callback_query_handler(func=lambda call: call.data == 'inst_sale_norki')
def callback_inline_lvl29(call):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Инстаграм', url='https://www.instagram.com/superlombard_astana/')
    markup.add(btn_my_site)
    if call.message:
        if call.data == "inst_sale_norki":
            bot.send_message(call.message.chat.id, "Нажмите на кнопку и перейди на наш профиль в инстаграм.", reply_markup = markup)

@bot.callback_query_handler(func=lambda call: call.data == 'fil_adress')
def callback_inline_lvl30(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "fil_adress":
            bot.send_message(call.message.chat.id, text = "Кокшетау ул. Абая 116, стадион «Окжетпес», 33 45 57\n Кокшетау ул. Абая 116,стадион «Окжетпес», 33 45 57\n Кокшетау ул. Абая 175, магазин Экспресс, 31 93 50\n Кокшетау ул. Гагарина 49,ТД Империал, 25 07 66\n Кокшетау пр.Аблай-Хана 30-31,возле маг. «Жаксы», 42 43 08\n Кокшетау мкрн. Боровской 53,маг. Тамерлан, 33 32 17\n Кокшетау пр. Нурсултана Назарбаева 64, 33 49 01\n Кокшетау ул. Достык 22, ТД Темирлан, 33 05 79\n Кокшетау ул. Мактая Сагдиева 48, 51 18 59\n Астана п-т Богенбай батыра 31, вп/1, 87076316509\n Астана ул. Петрова 23, 36-42-19\n Астана ул. Желтоксана 32, 32-85-90\n  Астана ул. Иле 30, маг. Тандем,29-97-83\n Астана ул. 189, маг. Даулет, 87072017340\n Алматы ул. Шолохова 4\n Алматы с.Туздыбастау ул. Алдабергенова 15\n")

@bot.callback_query_handler(func=lambda call: call.data == 'fil_ysl')
def callback_inline_lvl31(call):
    markup = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Золото", callback_data="fil_ysl_gold")
    callback_button_1 = types.InlineKeyboardButton(text="Автомобиль", callback_data="fil_ysl_auto")
    callback_button_2 = types.InlineKeyboardButton(text="Техника и норковые шубы", callback_data="fil_ysl_norki")
    markup.add(callback_button)
    markup.add(callback_button_1)
    markup.add(callback_button_2)
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "fil_ysl":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вас приветствует «Super Ломбард»", reply_markup = markup)

@bot.callback_query_handler(func=lambda call: call.data == 'fil_ysl_gold')
def callback_inline_lvl32(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "fil_ysl_gold":
            bot.send_message(call.message.chat.id,
                             text="с 18 лет, при предъявлении документа удостоверяющий личность\n залог на 30 дней \n 0,2% за каждый день\n 0,4% пеня за каждый день\n доверенное лицо\n частичный выкуп\n гарантийный срок 30 дней\n")

@bot.callback_query_handler(func=lambda call: call.data == 'fil_ysl_auto')
def callback_inline_lvl33(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "fil_ysl_auto":
            bot.send_message(call.message.chat.id,
                             text="автомобиль иностранного производства с 1991 года выпуска(с правом и без права вождения)\n российские автомобили не старше 5 лет (с правом и без права вождения)\n")

@bot.callback_query_handler(func=lambda call: call.data == 'fil_ysl_norki')
def callback_inline_lvl34(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "fil_ysl_norki":
            bot.send_message(call.message.chat.id,
                             text="аудио - видео техника, согласно приказу «Расценки на ТНП»\n бытовая техника, согласно приказу «Расценки на ТНП»\n шубы норковые, цельные, в идеальном состоянии, средней и максимальной длины")

@bot.callback_query_handler(func=lambda call: call.data == 'recalc')
def callback_inline_lvl36(call):
    markup = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Список филиалов", callback_data="fil_recalc")
    callback_button_1 = types.InlineKeyboardButton(text="Контакты", callback_data="cont_recalc")
    callback_button_2 = types.InlineKeyboardButton(text="Онлайн-карта", callback_data="map_recalc")
    callback_button_3 = types.InlineKeyboardButton(text="Вернуться в предыдущее меню", callback_data="back")
    markup.add(callback_button)
    markup.add(callback_button_1)
    markup.add(callback_button_2)
    markup.add(callback_button_3)
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "recalc":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вас приветствует «Super Ломбард»", reply_markup = markup)

@bot.callback_query_handler(func=lambda call: call.data == 'trusted_face')
def callback_inline_lvl37(call):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Для данной услуги требуется операция перезалог', url='http://superlombard.kz')
    callback_button_1 = types.InlineKeyboardButton(text="Список филиалов", callback_data="fil_trusted_face")
    callback_button_2 = types.InlineKeyboardButton(text="Контакты", callback_data="cont_trusted_face")
    callback_button_3 = types.InlineKeyboardButton(text="Вернуться в предыдущее меню", callback_data="back")
    markup.add(btn_my_site)
    markup.add(callback_button_1)
    markup.add(callback_button_2)
    markup.add(callback_button_3)
    if call.message:
        if call.data == "trusted_face":
            bot.send_message(call.message.chat.id, "Нажмите на кнопку и перейдите на наш сайт.", reply_markup = markup)

@bot.callback_query_handler(func=lambda call: call.data == 'part_sale')
def callback_inline_lvl38(call):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Для данной услуги требуется операция перезалог', url='http://superlombard.kz')
    callback_button_1 = types.InlineKeyboardButton(text="Список филиалов", callback_data="fil_part_sale")
    callback_button = types.InlineKeyboardButton(text="Вернуться в предыдущее меню", callback_data="back")
    markup.add(btn_my_site)
    markup.add(callback_button_1)
    markup.add(callback_button)
    if call.message:
        if call.data == "part_sale":
            bot.send_message(call.message.chat.id, "Нажмите на кнопку и перейдите на наш сайт.", reply_markup = markup)

@bot.callback_query_handler(func=lambda call: call.data == 'prolong')
def callback_inline_lvl39(call):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Продление онлайн', url='http://superlombard.kz/login')
    callback_button = types.InlineKeyboardButton(text="Вернуться в предыдущее меню", callback_data="back")
    markup.add(btn_my_site)
    markup.add(callback_button)
    if call.message:
        if call.data == "prolong":
            bot.send_message(call.message.chat.id, "Нажмите на кнопку и перейдите на наш сайт.", reply_markup = markup)

@bot.callback_query_handler(func=lambda call: call.data == 'fil_recalc')
def callback_inline_lvl40(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "fil_recalc":
            bot.send_message(call.message.chat.id, text = "Кокшетау ул. Абая 116, стадион «Окжетпес», 33 45 57\n Кокшетау ул. Абая 116,стадион «Окжетпес», 33 45 57\n Кокшетау ул. Абая 175, магазин Экспресс, 31 93 50\n Кокшетау ул. Гагарина 49,ТД Империал, 25 07 66\n Кокшетау пр.Аблай-Хана 30-31,возле маг. «Жаксы», 42 43 08\n Кокшетау мкрн. Боровской 53,маг. Тамерлан, 33 32 17\n Кокшетау пр. Нурсултана Назарбаева 64, 33 49 01\n Кокшетау ул. Достык 22, ТД Темирлан, 33 05 79\n Кокшетау ул. Мактая Сагдиева 48, 51 18 59\n Астана п-т Богенбай батыра 31, вп/1, 87076316509\n Астана ул. Петрова 23, 36-42-19\n Астана ул. Желтоксана 32, 32-85-90\n  Астана ул. Иле 30, маг. Тандем,29-97-83\n Астана ул. 189, маг. Даулет, 87072017340\n Алматы ул. Шолохова 4\n Алматы с.Туздыбастау ул. Алдабергенова 15\n")

@bot.callback_query_handler(func=lambda call: call.data == 'fil_trusted_face')
def callback_inline_lvl41(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "fil_trusted_face":
            bot.send_message(call.message.chat.id, text = "Кокшетау ул. Абая 116, стадион «Окжетпес», 33 45 57\n Кокшетау ул. Абая 116,стадион «Окжетпес», 33 45 57\n Кокшетау ул. Абая 175, магазин Экспресс, 31 93 50\n Кокшетау ул. Гагарина 49,ТД Империал, 25 07 66\n Кокшетау пр.Аблай-Хана 30-31,возле маг. «Жаксы», 42 43 08\n Кокшетау мкрн. Боровской 53,маг. Тамерлан, 33 32 17\n Кокшетау пр. Нурсултана Назарбаева 64, 33 49 01\n Кокшетау ул. Достык 22, ТД Темирлан, 33 05 79\n Кокшетау ул. Мактая Сагдиева 48, 51 18 59\n Астана п-т Богенбай батыра 31, вп/1, 87076316509\n Астана ул. Петрова 23, 36-42-19\n Астана ул. Желтоксана 32, 32-85-90\n  Астана ул. Иле 30, маг. Тандем,29-97-83\n Астана ул. 189, маг. Даулет, 87072017340\n Алматы ул. Шолохова 4\n Алматы с.Туздыбастау ул. Алдабергенова 15\n")

@bot.callback_query_handler(func=lambda call: call.data == 'fil_part_sale')
def callback_inline_lvl42(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "fil_part_sale":
            bot.send_message(call.message.chat.id, text = "Кокшетау ул. Абая 116, стадион «Окжетпес», 33 45 57\n Кокшетау ул. Абая 116,стадион «Окжетпес», 33 45 57\n Кокшетау ул. Абая 175, магазин Экспресс, 31 93 50\n Кокшетау ул. Гагарина 49,ТД Империал, 25 07 66\n Кокшетау пр.Аблай-Хана 30-31,возле маг. «Жаксы», 42 43 08\n Кокшетау мкрн. Боровской 53,маг. Тамерлан, 33 32 17\n Кокшетау пр. Нурсултана Назарбаева 64, 33 49 01\n Кокшетау ул. Достык 22, ТД Темирлан, 33 05 79\n Кокшетау ул. Мактая Сагдиева 48, 51 18 59\n Астана п-т Богенбай батыра 31, вп/1, 87076316509\n Астана ул. Петрова 23, 36-42-19\n Астана ул. Желтоксана 32, 32-85-90\n  Астана ул. Иле 30, маг. Тандем,29-97-83\n Астана ул. 189, маг. Даулет, 87072017340\n Алматы ул. Шолохова 4\n Алматы с.Туздыбастау ул. Алдабергенова 15\n")

@bot.callback_query_handler(func=lambda call: call.data == 'cont_recalc')
def callback_inline_lvl43(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "cont_recalc":
            bot.send_message(call.message.chat.id, text = "E-Mail: s-super111@mail.ru\n тел: 8 (7162) 72-27-20\n Автоломбард, г. Кокшетау: +7 702 921 48 61\n Автоломбард, г. Астана: +7 778 001 72 52\n Головной офис: г.Кокшетау, ул.Пушкина 14")

@bot.callback_query_handler(func=lambda call: call.data == 'cont_trusted_face')
def callback_inline_lvl44(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "cont_trusted_face":
            bot.send_message(call.message.chat.id, text = "E-Mail: s-super111@mail.ru\n тел: 8 (7162) 72-27-20\n Автоломбард, г. Кокшетау: +7 702 921 48 61\n Автоломбард, г. Астана: +7 778 001 72 52\n Головной офис: г.Кокшетау, ул.Пушкина 14")

if __name__ == '__main__':
    bot.polling()

