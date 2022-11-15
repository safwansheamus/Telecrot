import telebot
from cgitb import text
from urllib import response
from telebot import *
from tokenize import Token
from youtubesearchpython import VideosSearch
# import mysql.connector
# mydb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     passwd='',
#     database='data_siswa',
# )
# sql = mydb.cursor()

v1 = "Hai Iam Jiyyo Bot"
v2 = "ABCD"
v3 = "EFGH"
v4 = "XXXX"
v5 = "0000"

list = [v1, v2, v3, v4, v5]

Token = "5746410589:AAGxyUzlYk8OtkzYP0FDDpZ-llnSoO9sMy8"
jihyo = telebot.TeleBot(Token)
print("The bot is ready")


@jihyo.message_handler(commands=["start"])
def start(message):
    jihyo.reply_to(message, random.choice([list]))


@jihyo.message_handler(commands=["info"])
def help(message):
    jihyo.send_message(message.chat.id, "jiyyo bot is ready to service you")


@jihyo.message_handler(commands=["find"])
def find(message):
    data = message.text
    video = VideosSearch(data.replace("/find", ""),
                         limit=3)
    x = video.result()

    for i in range(3):
        judul = x['result'][i]['title']
        url = x['result'][i]['link']
        jihyo.send_message(message.chat.id, judul+"\n"+url)


jihyo.polling(none_stop=True, interval=0)

# # absen


# @bot.message_handler(commands=['absen'])
# def absen(message):
#     texts = message.text.split(' ')
#     tanggal_hadir = texts[1]

#     sql.execute("select nomor_induk, nama_siswa, kelas_siswa from data_siswa_absen where tanggal_hadir = '{}'"
#                 .format(tanggal_hadir))
#     hasil_sql = sql.fetchall()
#     print(hasil_sql)

#     pesan_balasan = ''
#     for i in hasil_sql:
#         pesan_balasan = pesan_balasan + str(i) + '\n'

#         bot.reply_to(message, pesan_balasan)


jihyo.polling()
