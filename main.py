import requests
import json
import random
from flask import request
from flask import Flask
from flask import Response
import os
url='https://api.telegram.org/bot1675079518:AAE954m5mol2ejn8m1aobvYebTzRQ28ALkE/'
app = Flask(__name__) #vasete barname ba server

def get_all_updates():
    global url
    response = requests.get(url + 'getUpdates')
    return response.json()

def last_update(data):
    result = data['result']
    last_index_number = len(result) - 1
    return result[last_index_number]

def get_chat_id(update):
    return update['message']['chat']['id']

def send_message(chat_id, text):
    global url
    send_data = {'chat_id': chat_id, 'text': text}
    response = requests.post(url + 'sendMessage', send_data)
    return response

def send_photo(chat_id, photo):
    global url
    data = {'chat_id': chat_id}
    myfile = {'photo': photo}
    response = requests.post(url + 'sendPhoto', data=data, files=myfile)
    return response

def game(target, n):
    target = int(target)
    n = int(n)
    if n > target:
        return 'kuchektr ast'
    elif n < target:
        return 'bozorgtr ast'
    else:
        return 'barabar'

def write_json(data, fileName='response.json'):
    with open(fileName, 'w') as f: #ba with minevisim ke moshkelate zamani baraye barname pish nayad
        json.dump(data, f, indent=4, ensure_ascii=False) # indent baraye ghashangie khoroji E ast ke mikhinimesh az page

def read_json(fileName='response.json'):
    with open(fileName, 'r') as f:
        dic = json.load(f)
    return dic
'''
@app.route('/', methods=['POST', 'GET']) #route kardan
def index():
    if request.method == 'POST':
        msg = request.get_json()
        chatid = str(msg['message']['chat']['id'])
        message = msg['message'].get('text', '') #message = msg['message']['text']
        if message == '/start':
            send_message(chatid, 'سلام، خوش آمدید:)')
            send_message(chatid, 'لطفا متن مورد نظر خود را وارد کنید.')
            send_message(chatid, 'اگر مطلب دیگری نبود "پایان" را ارسال کنید.')
            olderCommands = read_json()
            olderCommands[chatid] = []
            write_json(olderCommands)
        elif message.isalpha():
            olderCommands = read_json()
            list_user = olderCommands.get(chatid, [])
            if isinstance(list_user, list):
                print(len(list_user))
            if not isinstance(list_user, list):
                send_message(chatid, 'etelat nadorst ast')
            send_message(chatid, 'بسیار خوب، موفق باشید.')

        return Response('ok', status=200) #for server

    else:
        return '<h1>aleykomosalam<h1>'
'''

if __name__ == "__main__":
    olderCommands = {}
    write_json(olderCommands)
    data = get_all_updates()
    last = last_update(data)
    chat_id = get_chat_id(last)
    send_message(chat_id, 'سلام، خوش آمدید:)')
    send_message(chat_id, 'لطفا متن مورد نظر خود را وارد کنید.')
    send_message(chat_id, 'اگر مطلب دیگری نبود "پایان" را ارسال کنید.')
    send_message(chat_id, 'بسیار خوب، موفق باشید.')
    # send_photo(chat_id, open('120077896.png', 'rb'))
    print()
    # app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
