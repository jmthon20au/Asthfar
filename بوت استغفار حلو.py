#لاتلعب بلمكاتب ابددد
import telebot
from telebot import types
bot = telebot.TeleBot('7108337344:AAF4QOOyXbDyqdK1DTngkCaIR0nl3Ly69Wg')
k = types.InlineKeyboardMarkup()
k1 = types.InlineKeyboardButton("•اضغط هنا للاستغفار•",callback_data="a1")
k.add(k1)
@bot.message_handler(commands=['start'])
def hej(message):
 bot.send_message(message.chat.id,"اهلا بيك في بوت الاستغفار اذا لم تعرف طريقة استخدام البوت اكتب /help ، ارسل /chat للتواصل مع المطور",reply_markup=k)
 
 
@bot.message_handler(commands=['help'])
def hej(message):
 bot.send_message(message.chat.id,"فقط اضغط على اضغط هنا للاستغفار واستغفر 👇🏻 .",reply_markup=k)#تكدر تشيل help وتخلي اي امر وتغير الكتابة
 
 @bot.message_handler(commands=['chat'])
 def hej(message):
  bot.send_message(message.chat.id,"اهلا بك .. حساب المطور : @altaee_z .. قناة المطور : @my00002",reply_markup=k)
 
@bot.callback_query_handler(func=lambda call : True)
def callback(call):
 if call.data == "a1":
  a1(call.message)
def a1(message):
 i = open("lk.txt","a+")
 id = message.from_user.id
 i.write(f"{id}\n")
 i.close()
 n = open("lk.txt","r")
 ss = len(n.readlines())
 n.close()
 k = types.InlineKeyboardMarkup()
 k.add(k1)
 bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="انطق الان ----> الحمدلله ، استغفرالله ، اللهم صل على محمد وال محمد 🤍 :  〈{}〉".format(ss),reply_markup=k) #تكدر تغير الكتابة الي موجوده بس لتشيل (")
bot.polling()