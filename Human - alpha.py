import random
import requests # Для отправки документов / скринов
import os
from PIL import ImageGrab # Для получения скриншота
import platform # Для получения информации о ПК
import telebot
import time
import webbrowser
import telebot, wikipedia, re
import subprocess
import time
from tkinter import messagebox
import sys
from fuzzywuzzy import fuzz
# Создаем бота, пишем свой токен
bot = telebot.TeleBot('6965354150:AAGD70zqpi2utEu-BJRWuvvh7Zh6jc13R2Q')
# Устанавливаем русский язык в Wikipedia
wikipedia.set_lang("ru")
# Загружаем список фраз и ответов в массив
mas=[]
if os.path.exists('data/boltun.txt'):
    f=open('data/boltun.txt', 'r', encoding='UTF-8')
    for x in f:
        if(len(x.strip()) > 2):
            mas.append(x.strip())
    f.close()
    
# Создаем переводчик

# Задаем исходные язык и целевой язык
src = 'en'
dest = 'ru'
# Чистим текст статьи в Wikipedia и ограничиваем его тысячей символов
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        # Получаем первую тысячу символов
        wikitext=ny.content[:1000]
        # Разделяем по точкам
        wikimas=wikitext.split('.')
        # Отбрасываем всЕ после последней точки
        wikimas = wikimas[:-1]
        # Создаем пустую переменную для текста
        wikitext2 = ''
        # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
        for x in wikimas:
            if not('==' in x):
                    # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        # Теперь при помощи регулярных выражений убираем разметку
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        # Возвращаем текстовую строку
        return wikitext
    # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
    except Exception as e:
        return 'Я не смог найти информацию об этом!{{{(>_<)}}}'
# С помощью fuzzywuzzy вычисляем наиболее похожую фразу и выдаем в качестве ответа следующий элемент списка
def answer(text):
    try:
        text=text.strip()
        if os.path.exists('data/boltun.txt'):
            a = 0
            n = 0
            nn = 0
            for q in mas:
                if('u: ' in q):
                    # С помощью fuzzywuzzy получаем, насколько похожи две строки
                    aa=(fuzz.token_sort_ratio(q.replace('u: ',''), text))
                    if(aa > a and aa!= a):
                        a = aa
                        nn = n
                n = n + 1
            s = mas[nn + 1]
            return s
        else:
            return 'Ошибка'
    except:
        return 'Ошибка программного кода. Err_241'  
# Команда «Старт»
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_chat_action(m.chat.id, 'typing')
    time.sleep(3)
    bot.send_message(m.chat.id, f'Привет, [{m.from_user.first_name} {m.from_user.last_name}] Я на связи. Напиши мне Привет - что бы начать со мной общение, или же напиши /help что бы узнать информацию обо мне)' .format(m.from_user))
@bot.message_handler(commands=["info"])
def info(m, res=False):
    bot.send_chat_action(m.chat.id, 'typing')
    time.sleep(3)
    bot.send_message(m.chat.id, "Мои функции:\n/help - узнать обо мне;\n/wiki - узнать значение слова на wikipedia;\n/photo - прислать рандомное фото с ПК;")
@bot.message_handler(commands=["help"])
def help(m, res=False):
    bot.send_chat_action(m.chat.id, 'typing')
    time.sleep(3)
    bot.send_message(m.chat.id, 'Привет. Меня зовут Никита. И я увлекаюсь изучением Планеты Земля и всех наук. Я постараюсь ответить на твои вопросы. Если я что-то не знаю, я могу написать тебе ответ на другой вопрос, а не на твой. Извини уж за это. Я постараюсь изучить по больше, и ответить на твой вопрос позже. Что бы начать общаться со мной напиши слово "Привет"')
@bot.message_handler(commands=['anime'])
def anime(message):
    bot.send_photo(message.chat.id, photo = 'https://uprostim.com/wp-content/uploads/2021/03/anime-devushki_00017.jpg')
    time.sleep(1)
    bot.send_photo(message.chat.id, photo = 'https://w.forfun.com/fetch/ed/ed69ef739a69b03d654032470a18caba.jpeg')
    time.sleep(1)    
    bot.send_photo(message.chat.id, photo = 'https://avatars.mds.yandex.net/i?id=4632ff42dbcb92c290ff690a25dcdf4a1fbe4c8a-9225226-images-thumbs&n=13') 
    time.sleep(1.5)    
    bot.send_photo(message.chat.id, photo = 'https://avatars.mds.yandex.net/i?id=f5cbf8e150bd6ccf10359531c4574408ef621f65-9151930-images-thumbs&n=13') 
    time.sleep(1)    
    bot.send_photo(message.chat.id, photo = 'https://avatars.mds.yandex.net/i?id=34266b9ebd6764d98e5e2dd6dc41b4738a437b08-7593439-images-thumbs&n=13') 
    time.sleep(2)    
    bot.send_photo(message.chat.id, photo = 'https://avatars.mds.yandex.net/i?id=373c8ef5578ec10569f62d7599ce584030de42b2-9678040-images-thumbs&n=13') 
@bot.message_handler(commands=['start'])
def help(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(3)
    bot.send_message(message.chat.id, 'Привет, я бот разработанный компанией ALpha Server System при поддержке WAIFY VZ Corporation. \nМои функции:\n/start - узнать обо мне;\n/photo - отправить рандомную фотографию;')
@bot.message_handler(commands=['comp'])
def comp(m):
    msg = bot.send_message(m.chat.id, 'Text')
    time.sleep(1)
    bot.edit_message_text(chat_id = m.chat.id, message_id = msg.message_id, text = 'Edited text')
    time.sleep(1)
@bot.message_handler(commands=['photo'])
def start(message):
    photo = open('test/' + random.choice(os.listdir('test')), 'rb')
    bot.send_photo(message.chat.id, photo, caption = 'Лови')
@bot.message_handler(commands='error')
def error(message):
    message_1 = bot.send_message(message.from_user.id, 'Введите текст:')
    bot.register_next_step_handler(message_1, error_2)
def error_2(message):
    bot.send_message(message.chat.id, 'Ваши слова отправлены на серверную машину ALpha v2.0')
    messagebox.showerror('ALpha Server System', message.text)
@bot.message_handler(commands='site')
def site(message):
    url = bot.send_message(message.from_user.id, 'Введите ссылку:')
    bot.register_next_step_handler(url, after_site_2)
def after_site_2(message):
    print(message.text)
    bot.send_message(message.chat.id, 'Открываю!')
    webbrowser.open(message.text)
@bot.message_handler(commands='wiki')
def wiki(message):
    msg = bot.send_message(message.from_user.id, 'Введите запрос:')
    bot.register_next_step_handler(msg, after_text_2)
def after_text_2(message):
    print(message.text)
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, getwiki(message.text))
# Получение сообщений от юзера
@bot.message_handler(commands='stop.5')
def stop(message):
    bot.send_message(message.chat.id, 'Внимание! Система завершит свою работу через 5 минут!')
    time.sleep(300)
@bot.message_handler(commands='shutdown_a')
def cans(message): 
    os.system("shutdown /a")
@bot.message_handler(commands='shutdown_pc.120')
def res(message): 
    os.system("shutdown /s /t 120")
@bot.message_handler(commands='sleep')
def sleep(message): 
    os.system("shutdown /h")
@bot.message_handler(commands='shutdown')
def res(message): 
    os.execl(sys.executable, sys.executable, *sys.argv) 
@bot.message_handler(content_types=["text"])
def handle_text(message):
    #Лох
    if message.text.lower()=='лох':
        bot.delete_message(message.chat.id, message.message_id)
    #Что делаешь
    elif message.text.lower()=='что делаешь':
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(3)
        foo = ['Играю в игры на компьютере.', 'Сижу у окна и слушаю классику.', 'Решил почитать книгу о Python.', 'Я только собирался спросить тебя об этом.', 'Просто играю с (Адой). Это мой хорёк, питомец.', 'Думал о том, чтобы пойти на обед.'] 
        bot.send_message(message.chat.id, random.choice(foo))
    elif message.text.lower()=='что делаешь?':
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(3)
        foo = ['Играю в игры на компьютере.', 'Сижу у окна и слушаю классику.', 'Решил почитать книгу о Python.', 'Я только собирался спросить тебя об этом.', 'Просто играю с (Адой). Это мой хорёк, питомец.', 'Думал о том, чтобы пойти на обед.'] 
        bot.send_message(message.chat.id, random.choice(foo))
    elif message.text.lower()=='чд?':
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(3)
        foo = ['Играю в игры на компьютере.', 'Сижу у окна и слушаю классику.', 'Решил почитать книгу о Python.', 'Я только собирался спросить тебя об этом.', 'Просто играю с (Адой). Это мой хорёк, питомец.', 'Думал о том, чтобы пойти на обед.'] 
        bot.send_message(message.chat.id, random.choice(foo))
    elif message.text.lower()=='чд':
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(3)
        foo = ['Играю в игры на компьютере.', 'Сижу у окна и слушаю классику.', 'Решил почитать книгу о Python.', 'Я только собирался спросить тебя об этом.', 'Просто играю с (Адой). Это мой хорёк, питомец.', 'Думал о том, чтобы пойти на обед.'] 
        bot.send_message(message.chat.id, random.choice(foo))
    elif message.text.lower()=='ч д?':
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(3)
        foo = ['Играю в игры на компьютере.', 'Сижу у окна и слушаю классику.', 'Решил почитать книгу о Python.', 'Я только собирался спросить тебя об этом.', 'Просто играю с (Адой). Это мой хорёк, питомец.', 'Думал о том, чтобы пойти на обед.'] 
        bot.send_message(message.chat.id, random.choice(foo))
    elif message.text.lower()=='ч д':
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(3)
        foo = ['Играю в игры на компьютере.', 'Сижу у окна и слушаю классику.', 'Решил почитать книгу о Python.', 'Я только собирался спросить тебя об этом.', 'Просто играю с (Адой). Это мой харёк, питомец.', 'Думал о том, чтобы пойти на обед.'] 
        bot.send_message(message.chat.id, random.choice(foo))
    #Пидор
    elif message.text.lower()=='пидор':
        bot.delete_message(message.chat.id, message.message_id)
    # Запись логов
    f=open('data/' + str(message.chat.id) + '_log.txt', 'a', encoding='UTF-8')
    s=answer(message.text)
    f.close()
    # Отправка ответа
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(3)
    bot.send_message(message.chat.id, s)
# Запускаем бота
bot.polling(none_stop=True, interval=0)