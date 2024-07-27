# HOW TO MAKE YOUR TELEGRAM BOT IN PYTHON?
# You can put any texts - both Russian and English.
# This code is mainly for beginners.

# FOR INSTALL LIBRARY:
# - OPEN A CMD
# - ENTER "pip install pyTelegramBotAPI"

#-------- THE IMPORTANT LIBRARIES FOR THE BOT --------------

import telebot
from telebot import types

#----------------------------------------------------------

import time
import random
import emoji

# <var of bot>.send_message(message.chat.id, "any text") - A COMMAND OF SENDING MESSAGE BY BOT IN CURRENT CHAT

# MAKE THE BOT IN https://t.me/BotFather.

<var of bot> (bot) = telebot.TeleBot("<YOUR TELEGRAM BOT TOKEN>") # YOU CAN SEE A TOKEN IN https://t.me/BotFather.


gr = ["Приветик :3", "Кусь ^^", "Хай))", "Хэллоу ❤"] # LIST OF GREETINGS
pictures = ["https://i.pinimg.com/236x/e2/59/0b/e2590bfea8680cb14365ca104f38aed3.jpg"] # LIST OF PICTURES
musics = ["C:/Users/123/Desktop/Telegram Bot Telebot & Files to Bot/Carlagan - Hooley Gun.mp3", "C:/Users/123/Desktop/Telegram Bot Telebot & Files to Bot/Die Antwoord - Coockie Thumper.mp3",
          "C:/Users/123/Desktop/Telegram Bot Telebot & Files to Bot/Lenka - Blue Skies (Revoke Remix).mp3", "C:/Users/123/Desktop/Telegram Bot Telebot & Files to Bot/Lx24 - Танцы под луной.mp3",
          "C:/Users/123/Desktop/Telegram Bot Telebot & Files to Bot/SubZero - Press Start.mp3", "C:/Users/123/Desktop/Telegram Bot Telebot & Files to Bot/Waterflame - Jumper.mp3",
          "C:/Users/123/Desktop/Telegram Bot Telebot & Files to Bot/elza gina - Кругами.mp3", "C:/Users/123/Desktop/Telegram Bot Telebot & Files to Bot/elza gina - Портретами.mp3"
          "C:/Users/123/Desktop/Музыка от Лизы.mpeg"] # LIST OF MUSICS
rps = ["Камень", "Ножницы", "Бумага"] # "ROCK-PAPER-SCISSORS" GAME :D (LINE 305)


#------------- FUNCTION FOR LAUNCHING A BOT WITH A /START COMMAND ---------

@bot.message_handler(commands=['start']) # CREATE A /START COMMAND
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Help") # CREATE A BUTTON
    markup.add(btn1) # ADD A BUTTON
    bot.send_message(message.chat.id, text="Приветик, {0.first_name} давай пообщаемся? ^^".format(message.from_user), reply_markup=markup)

# {0.first_name} IS A NAME TELEGRAM ACCOUNT

@bot.message_handler(content_types=['text'])

#--------- REPLYING BY BOT ON USER MESSAGES -------------

def text_messages(message): # FUNCTION FOR REPLYING BY BOT ON ANY MESSAGES BY USERS
    <var of message texts by ures> (mes_text) = message.text.lower()
    if mes_text.find("прив") >=0 or mes_text.find("приветик") >=0 or mes_text == "ку" or mes_text.find("ghbd") >= 0 or mes_text.find("хай") >= 0: # CONDITION FOR REPLY
        bot.send_message(message.chat.id, <replying message> '''random.choice(gr)''') # IF CONDITION IS TRUE, THE BOT WILL REPLY

    elif mes_text.find("пикч") >=0 or mes_text.find("картинк") >=0 or mes_text.find("арт") >=0:
        bot.send_photo(message.chat.id, random.choice(pictures)) # LIST OF PICTURES

    elif mes_text.find("вступил") >=0:
        bot.send_message(message.chat.id, emoji.emojize("Приветики! Ты вступил(а) в нашу беседу, добро пожаловать! :smiling_face_with_smiling_eyes:", use_aliases=True)'''REPLYING MESSAGE WITH EMOJI''')

    elif mes_text == "хорошо" or mes_text == "отлично":
        bot.send_message(message.chat.id, emoji.emojize("Ну и славно :smiling_face_with_smiling_eyes:", use_aliases=True))

    elif mes_text == "плохо" or mes_text == "ужасно"or mes_text.find("так себе") >=0:
        bot.send_message(message.chat.id, "Почему? Что случилось?..(")

    elif mes_text.find("спок") >=0:
        bot.send_message(message.chat.id, emoji.emojize("Спокойной ночи! :smiling_face_with_smiling_eyes: ❤", use_aliases=True))

    elif mes_text.find("ты даун") >=0:
        bot.send_message(message.chat.id, emoji.emojize("Почему ты так думаешь? :crying_face:", use_aliases=True))


    elif mes_text.find("доброе") >=0 or mes_text.find("утро") >=0 or mes_text.find("добренькое") >=0 or mes_text.find("утречко") >=0:
        bot.send_message(message.chat.id, "Доброе утро! ❤\nКак спалось?)")

    elif mes_text.find("я тебя люблю") >=0:
        bot.send_message(message.chat.id, emoji.emojize("Я тебя тоже люблю :smiling_face_with_smiling_eyes: ❤❤❤", use_aliases=True))

#---------------- THE PRIMITIVE SWEARS FILTER --------------------------------------------------------------------------------

    elif mes_text == "бля" or mes_text.find("пидо") >=0 or mes_text.find("пида") >=0 or mes_text == "бл" or mes_text == "еб" or mes_text.find("пиз") >=0 or mes_text.find("хуй") >=0 \
         or mes_text.find("хуя") >=0 or mes_text.find("хуеть") >=0 or mes_text.find("жоп") >=0 or mes_text.find("сука") >=0 or mes_text.find("блять") >=0 or mes_text == "блядь" \
         or mes_text == "блять" or mes_text == "нах" or mes_text.find("науй") >=0 or mes_text.find("нахой") >=0 or mes_text.find("гитлер") >=0 or mes_text.find("наци") >=0 \
         or mes_text.find("1488") >=0 or mes_text.find("14 88") >=0 or mes_text.find("пидр") >=0 or mes_text.find("fuck"):
        bot.delete_message(message.chat.id, message.message_id) # DELETE MESSAGE WHICH SENT BY USER
        bot.send_message(message.chat.id, emoji.emojize(message.from_user.first_name+", материться плохо! :angry_face:", use_aliases=True))

#-----------------------------------------------------------------------------------------------------------------

    elif mes_text.find("доброе") >=0 or mes_text.find("доброе утро") >=0:
        bot.send_message(message.chat.id, "Доброе утречко! <3")

    elif mes_text.find("муз") >=0 or mes_text.find("music") >=0: # LIST OF MUSICS
        audio = open(random.choice(musics), 'rb')
        bot.send_message(message.chat.id, "Немножечко подожди, отправляю музычку <3")
        bot.send_audio(message.chat.id, audio)
        audio.close()
        time.sleep(1)
        bot.send_message(message.chat.id, emoji.emojize("Держи, слушай на здоровье :smiling_face_with_smiling_eyes:", use_aliases=True))

    elif mes_text.find("лох") >=0:
        bot.send_message(message.chat.id, emoji.emojize("Сам ты лох! :angry_face:", use_aliases=True))

    elif mes_text == "?":
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEFbxVi58RqKUaBHvAhPX8oXa46RT9zQgACnxQAAujW4hJNA6btYiLX9ikE")

    elif mes_text.find("глупый бот") >=0:
        bot.send_message(message.chat.id, emoji.emojize("Нет, это неправда, сам глупый! :face_with_symbols_on_mouth:", use_aliases=True))


#--------- ALPHABET (RUSSIAN) :D ----------------------------

    elif mes_text == "а":
        bot.send_message(message.chat.id, "б")

    elif mes_text == "б":
        bot.send_message(message.chat.id, "в")

    elif mes_text == "в":
        bot.send_message(message.chat.id, "г")

    elif mes_text == "г":
        bot.send_message(message.chat.id, "д")

    elif mes_text == "д":
        bot.send_message(message.chat.id, "е")

    elif mes_text == "е":
        bot.send_message(message.chat.id, "ё")

    elif mes_text == "ё":
        bot.send_message(message.chat.id, "ж")

    elif mes_text == "ж":
        bot.send_message(message.chat.id, "з")

    elif mes_text == "з":
        bot.send_message(message.chat.id, "и")

    elif mes_text == "и":
        bot.send_message(message.chat.id, "й")

    elif mes_text == "й":
        bot.send_message(message.chat.id, "к")

    elif mes_text == "к":
        bot.send_message(message.chat.id, "л")

    elif mes_text == "л":
        bot.send_message(message.chat.id, "м")

    elif mes_text == "м":
        bot.send_message(message.chat.id, "н")

    elif mes_text == "н":
        bot.send_message(message.chat.id, "о")

    elif mes_text == "о":
        bot.send_message(message.chat.id, "п")

    elif mes_text == "п":
        bot.send_message(message.chat.id, "р")

    elif mes_text == "р":
        bot.send_message(message.chat.id, "с")

    elif mes_text == "с":
        bot.send_message(message.chat.id, "т")

    elif mes_text == "т":
        bot.send_message(message.chat.id, "у")

    elif mes_text == "у":
        bot.send_message(message.chat.id, "ф")

    elif mes_text == "ф":
        bot.send_message(message.chat.id, "х")

    elif mes_text == "х":
        bot.send_message(message.chat.id, "ц")

    elif mes_text == "ц":
        bot.send_message(message.chat.id, "ч")

    elif mes_text == "ч":
        bot.send_message(message.chat.id, "ш")

    elif mes_text == "ш":
        bot.send_message(message.chat.id, "щ")

    elif mes_text == "щ":
        bot.send_message(message.chat.id, "ъ")

    elif mes_text == "ъ":
        bot.send_message(message.chat.id, "ы")

    elif mes_text == "ы":
        bot.send_message(message.chat.id, "ь")

    elif mes_text == "а":
        bot.send_message(message.chat.id, "б")

    elif mes_text == "ь":
        bot.send_message(message.chat.id, "э")

    elif mes_text == "э":
        bot.send_message(message.chat.id, "ю")

    elif mes_text == "ю":
        bot.send_message(message.chat.id, "я")

    elif mes_text == "я":
        bot.send_message(message.chat.id, "ты)")

    elif mes_text == "ты":
        bot.send_message(message.chat.id, "дя, я))")

#--------------------------------------------------------------------------

#--------- OTHER BOT COMMANDS -----------------------

    elif mes_text == "help" or mes_text.find("/help") >=0:
        bot.send_message(message.chat.id, text="Списочек всех известных команд:\n\n" \
                         "\n⇒ /rules - Правила\n⇒ /dev - Разработка ботика\n⇒ /about - О ботике\n⇒ /support - Тех. поддержка" \
                         "\n⇒ /roll - Генерация случайного числа (макс. 100)\n⇒ /rps - Игра 'Камень, Ножницы, Бумага' (бета-тест)" \
                         "\n\nЭмоции:\n⇒ /cry - Плач\n⇒ /laugh - Смех\n⇒ /angry - Злоба\n⇒ /yawn - Зевание\n⇒ /moai - Каменное лицо (Истукан)\n⇒ /please - Умолять\n⇒ /smirk - Ухмылка" \
                         "\n⇒ /cold - Холод\n⇒ /explosive - Взрыв мозга\n⇒ /think - Думать\n⇒ /clown - Клоун" \
                         "\n⇒ /ill - Болезнь\n⇒ /zany - Безумие\n⇒ /notbelieve - Не верю\n⇒ /party - Праздник\n⇒ /sleep - Сон" \
                         "\n\nСсылочки:\n⇒ /group - Наш канал о Fantasy Town\n⇒ /gamelink - Ссылочка на игру Fantasy Town\n⇒ /discord - Наш Discord-канал Fantasy Town" \
                         "\n⇒ /vk - Наша группа ВКонтакте о Fantasy Town")
        bot.delete_message(message.chat.id, message.message_id)

    elif mes_text.find("/about") >= 0:
        bot.send_message(message.chat.id, emoji.emojize("Я Fantasy Town, Телеграм-бот, очень люблю общаться с людьми! Если хочешь, можем общаться днями напролёт!)))" \
                         "\n\nЯ умею немного, но с каждым днём становлюсь умнее. Научи меня чему-нибудь, я буду очень благодарен!" \
                         "\n\nТакже есть много других различных прикольных команд)))" \
                         "\n\n• Введи команду /dev чтобы узнать обо мне в плане программирования." \
                         "\n• Введи команду /help или 'помощь', чтобы просмотреть весь списочек известных команд." \
                         "\n\nЕсли у Вас есть идеи для бота, пожалуйста, напишите автору (/support). Автор сделает всё, что сможет!"+' :grinning_face_with_smiling_eyes:', use_aliases=True))


    elif mes_text.find("/dev") >= 0 or mes_text == "дев": #-------ПОМЕТКА--------
        bot.send_message(message.chat.id, "Я полностью запрограммирован на языке программирования Python.\n\nВерсия на данный момент: 0.13.2.\n\nVPS/VDS отсутствует.")

    elif mes_text == "апдейт": #-------ПОМЕТКА---------
        bot.send_message(message.chat.id, "Что новенького?\n\n В версии 0.12.5:\n • Очищен журнал изменений\n • Улучшен функционал бота\n • Обновлён фильтр нецензурных слов\n • Добавлена панель с кнопками (см. внизу)\n • Подкорректированы некоторые сообщения\n • Расширен интеллект бота\n • Добавлено больше картиночек и музыки (пиши 'картинка'/'музыка'\n • Добавлены URL-кнопки\n • Переустановлен пакет pyTelegramBotAPI\n • Теперь бот распознаёт пользователя\n • Исправлены некоторые баги (фильтр нецензурных слов, приветствие, алфавит, команды, общение)\n • Добавлена команда /sss - Камень, Ножницы, Бумага" \
                         "\n\n В версии 0.13.2:\n • Обновлён журнал изменений\n • Обновлён список команд (/help)\n • Обновлён фильтр нецензурных слов\n • Обновлена игра 'Камень, ножницы, бумага' (/rps)\n • Обновлено сообщение /support\n • Добавлено 5 новых эмоций (/help)\n • Исправлены некоторые ошибки и недоработки\n • Обновлена функция эмоций.\n • Изменены условия для ответа на некоторые сообщения.")
        bot.delete_message(message.chat.id, message.message_id)

    elif mes_text.find("/performance") >=0:
        bot.send_message(message.chat.id, emoji.emojize("Если я отправил сообщение, значит всё отлично! :grinning_face_with_big_eyes:", use_aliases=True))
        bot.delete_message(message.chat.id, message.message_id)

#--------------------- BUTTONS WITH LINK ------------------------------

    elif mes_text.find("/group") >= 0:
        markup = types.InlineKeyboardMarkup() # CREATE A LINK FOR THE BUTTON
        url1 = types.InlineKeyboardButton("Fantasy Town", url='https://t.me/FantasyTownOfficialServer') # CREATE A BUTTON WITH A LINK
        markup.add(url1)# ADD A BUTTON (UNDER A GENERAL MESSAGE)
        bot.send_message(message.chat.id, "Вот ссылочка на нашу группу, обязательно подпишись ❤".format(message.from_user), reply_markup=markup) # SEND GENERAL MESSAGE

    elif mes_text.find("/support") >=0:
        markup = types.InlineKeyboardMarkup()
        url2 = types.InlineKeyboardButton("bodutop - Telegram", url='t.me/bodutop')
        markup.add(url2)
        vk = types.InlineKeyboardButton("bodutop - ВКонтакте", url='vk.com/bodutop')
        markup.add(vk)
        bot.send_message(message.chat.id, "По всем вопросам, предложениям, жалобам пиши автору бота ❤".format(message.from_user), reply_markup=markup)

    elif mes_text.find("/gamelink") >=0:
        markup = types.InlineKeyboardMarkup()
        url3 = types.InlineKeyboardButton("Fantasy Town Game", url='https://fantasytown.ca')
        markup.add(url3)
        bot.send_message(message.chat.id, "Ссылочка на наш сервер Fantasy Town! ❤".format(message.from_user), reply_markup=markup)

    elif mes_text.find("/discord") >=0:
        markup = types.InlineKeyboardMarkup()
        url4 = types.InlineKeyboardButton("Fantasy Town Discord", url='https://discord.gg/pTKpbkQV')
        markup.add(url4)
        bot.send_message(message.chat.id, "Ссылочка на наш Discord-сервер Fantasy Town! ❤".format(message.from_user), reply_markup=markup)

    elif mes_text.find("/vk") >=0:
        markup = types.InlineKeyboardMarkup()
        url5 = types.InlineKeyboardButton("Fantasy Town ВКонтакте", url='https://vk.com/fantasyuwu')
        markup.add(url5)
        bot.send_message(message.chat.id, "Ссылочка на нашу группу ВКонтакте о Fantasy Town! ❤".format(message.from_user), reply_markup=markup)
        

#----------------------------------------------------------------------
        

    elif mes_text.find("/rules") >=0:
        bot.send_message(message.chat.id, "Привет! Пожалуйста, соблюдай правила:\n1. Не матерись в нашей группе.\n2. Просьба соблюдать сетевой этикет!\n3. Не разжигай межнациональные/расовые/религиозные конфликты!\n4. Не отправляй материалы сексуального, наркотического и т.п. характера.\n5. Не злоупотребляй своими правами и возможностями!\n6. Разрешён флуд.\nНадеюсь, ты понял правила, приятного общения! ^^")

    elif mes_text.find("/roll") >=0 or mes_text.find("рол") >=0 or mes_text.find("число") >=0:
        number = random.randint(1, 100)
        text_end_roll_message = "из"
        one_hundred = 100
        output_text = "Rolled:"+" "+str(number)+" "+(text_end_roll_message)+" "+str(one_hundred)
        bot.send_message(message.chat.id, emoji.emojize(":game_die: "+output_text, use_aliases=True

#-----------------"ROCK-PAPER-SCISSORS" GAME (A PRIMITIVE VERSION)
    elif mes_text.find("/rps") >=0:
        rock = rps[0]
        scissors = rps[1]
        paper = rps[2]
        res = random.choice(rps)
        if res == rps[0]:
            bot.send_message(message.chat.id, emoji.emojize(':rock: '+"Камень"))
        elif res == rps[1]:
            bot.send_message(message.chat.id, emoji.emojize(':scissors: '+"Ножницы"))
        elif res == rps[2]:
            bot.send_message(message.chat.id, emoji.emojize(':roll_of_paper: '+"Бумага"))
        
#----------------------- BOT EMOTIONS :D ------------------------------------------

    elif mes_text.find("/angry") >=0:
        bot.send_message(message.chat.id, emoji.emojize(message.from_user.first_name+" злится :angry_face:", use_aliases=True))
        bot.delete_message(message.chat.id, message.message_id)

    elif mes_text.find("/laugh") >=0:
        bot.send_message(message.chat.id, emoji.emojize(message.from_user.first_name+" смеётся :face_with_tears_of_joy:", use_aliases=True))
        bot.delete_message(message.chat.id, message.message_id)

    elif mes_text.find("/yawn") >=0:
        bot.send_message(message.chat.id, emoji.emojize(message.from_user.first_name+" зевает :yawning_face:", use_aliases=True))
        bot.delete_message(message.chat.id, message.message_id)

    elif mes_text.find("/cry") >=0:
        bot.send_message(message.chat.id, emoji.emojize(message.from_user.first_name+" плачет :loudly_crying_face:", use_aliases=True))
        bot.delete_message(message.chat.id, message.message_id)

    elif mes_text.find("/moai") >=0:
        bot.send_message(message.chat.id, emoji.emojize(message.from_user.first_name+" ничего не понимает/в шоке от происходящего :moai:", use_aliases=True))
        bot.delete_message(message.chat.id, message.message_id)

    elif mes_text.find("/please") >=0:
        bot.send_message(message.chat.id, emoji.emojize(message.from_user.first_name+" умоляет :pleading_face:", use_aliases=True))
        bot.delete_message(message.chat.id, message.message_id)

    elif mes_text.find("/smirk") >=0:
        bot.send_message(message.chat.id, emoji.emojize(message.from_user.first_name+" ухмыляется :smirking_face:", use_aliases=True))
        bot.delete_message(message.chat.id, message.message_id)

    elif mes_text.find("/cold") >=0:
        bot.send_message(message.chat.id, emoji.emojize(message.from_user.first_name+" замёрз :cold_face:", use_aliases=True))
        bot.delete_message(message.chat.id, message.message_id)

    elif mes_text.find("/explosive") >=0:
        bot.send_message(message.chat.id, emoji.emojize("У "+message.from_user.first_name+" взорвался мозг :exploding_head:", use_aliases=True))
        bot.delete_message(message.chat.id, message.message_id)

    elif mes_text.find("/think") >=0:
        bot.send_message(message.chat.id, emoji.emojize(message.from_user.first_name+" думает :thinking_face:", use_aliases=True))
        bot.delete_message(message.chat.id, message.message_id)

    elif mes_text.find("/clown") >=0:
        bot.send_message(message.chat.id, emoji.emojize(message.from_user.first_name+" пошутил :clown_face:", use_aliases=True))
        bot.delete_message(message.chat.id, message.message_id)

    elif mes_text.find("/ill") >=0:
        bot.send_message(message.chat.id, emoji.emojize(message.from_user.first_name+" заболел :face_with_thermometer:", use_aliases=True))
        bot.delete_message(message.chat.id, message.message_id)

    elif mes_text.find("/zany") >=0:
        bot.send_message(message.chat.id, emoji.emojize(message.from_user.first_name+" сошёл с ума :zany_face:", use_aliases=True))
        bot.delete_message(message.chat.id, message.message_id)

    elif mes_text.find("/notbelieve") >=0:
        bot.send_message(message.chat.id, emoji.emojize(message.from_user.first_name+" не верит... :face_with_raised_eyebrow:", use_aliases=True))
        bot.delete_message(message.chat.id, message.message_id)

    elif mes_text.find("/party") >=0:
        bot.send_message(message.chat.id, emoji.emojize("У "+message.from_user.first_name+" сегодня праздник! :partying_face:", use_aliases=True))
        bot.delete_message(message.chat.id, message.message_id)

    elif mes_text.find("/sleep") >=0:
        bot.send_message(message.chat.id, emoji.emojize(message.from_user.first_name+" спит :sleeping:", use_aliases=True))
        bot.delete_message(message.chat.id, message.message_id)
        
#-----------------------------------------------------------------------------------------------

  ''' # else:
     #   bot.send_message(message.chat.id, "Something went wrong... \n\n\nError type: 7717 :/")'''
   

#----------------- SO THAT THE BOT DOES NOT DISCONNECT ------------------------

while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except:
        time.sleep(5)
