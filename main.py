import test, urllib, subprocess
import datetime as dt
from os import path
from telegram.ext import Updater
updater = Updater(token='638450968:AAEHASk3PQx7mDsVvs97FaF1vgpYFsbQSNM', use_context=True)
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!\n Also you can send me a voice message!")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

import speech_recognition as sr

def voice_recognition(update, context):
    print("Got a voice handler!")
#    print(update.message.voice.get_file().file_path)
    print(update.message.voice.get_file().file_path)
    TimeNow = dt.datetime.now()


    src_filename = update.message.from_user.username + "_" +str(TimeNow.year)+"-"+str(TimeNow.month)+"-"+str(TimeNow.day)+" "+str(TimeNow.hour)+":"+str(TimeNow.minute) + ".oga"
    urllib.urlretrieve(update.message.voice.get_file().file_path, src_filename)
    dest_filename = 'voice.wav'

    process = subprocess.call(['ffmpeg', '-i', src_filename, dest_filename])
    r = sr.Recognizer()
    AUDIO_FILE = path.join(path.dirname(path.realpath("main.py")), "voice.wav")
    with sr.AudioFile(AUDIO_FILE) as source:
        print("Try to got as a source")
        audio = r.record(source)
        subprocess.call(["rm","voice.wav"])
        subprocess.call(["mv","./"+src_filename,"./Voice_Storage"])
    try:
        print("Recognizing...")
        EngText = r.recognize_google(audio)
        RusText = test.translate(EngText)
        context.bot.send_message(chat_id=update.message.chat_id, text=RusText)
    except sr.UnknownValueError:
        print("Something is wrong!")
        context.bot.send_message(chat_id=update.message.chat_id, text="Could not understand audio")

from telegram.ext import MessageHandler, Filters
voice_handler = MessageHandler(Filters.voice, voice_recognition)
dispatcher.add_handler(voice_handler)

updater.start_polling()

