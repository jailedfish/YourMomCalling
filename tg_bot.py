import socket
import telebot
import argparse

token = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def dumpConf():
    global token

    cfg = ConfigParser().read('config.ini')

    token = cfg['BOT']['TOKEN']

pairs = {}
actions = {}
passw = {}

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'pair'])
def welcome_handler(msg):
    actions[message.chat.id] = 99
    bot.reply_to(msg, 'Hello, please enter ip of your gamer')
    actions[message.chat.id] = 1

@bot.message_handler(commands=['defpass, setDefaultPassword, pass'])
def defpass_handler(msg):
    actions[msg.chat.id] = 2
    bot.reply_to(msg, 'print new default password')

@bot.message_handler(commands=['call, run, send, start'])
    actions[msg.chat.id] = 3
    bot.reply_to(msg, 'Print password please')

@bot.message_handler()
def text_handler(msg):
    if actions[msg.chat.id] == 1:
        pairs[message.chat.id] = msg.text
        bot.reply_to(msg, 'You paired with '+ msg.text)
        actions[msg.chat.id] = 0
    
    if actions[msg.chat.id] == 2:
        passw[msg.chat.id] == msg.text
        bot.reply_to(msg, 'You changed default password to ' + msg.text)
        actions[msg.chat.id] = 0

    if actions[msg.chat.id] == 3:
        
        try:
            s.connect((pairs[msg.chat.id]), 4096)
            s.sendall(msg.text.encode())
            res = s.resv(1024).decode()
            if res == 'e':
                bot.reply_to(msg, 'wrong password')
            elif res == 's':
                s.sendall(b'call')
                bot.repy_to(msg, 'send sus')

