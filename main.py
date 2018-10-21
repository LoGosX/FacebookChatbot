import os
import sys
import json
import threading
from queue import Queue
import requests
import time

from flask import Flask, request

from my_client import run

app = Flask(__name__)

messages_queue = Queue()

main_thread = None
keep_awake_thread = None

can_start = True


def keep_awake():
    while True:
        requests.get(os.environ['HEROKU_APP_URL'])
        time.sleep(5 * 60)

@app.route('/')
def webhook():
    return 'Okey', 200

@app.route('/start')
def start():
    global main_thread, messages_queue, can_start, keep_awake_thread
    if can_start:
        main_thread = threading.Thread(target=run, args=(messages_queue,))
        main_thread.start()
        can_start = False
    
    if not keep_awake_thread:
        keep_awake_thread = threading.Thread(target=keep_awake)
        keep_awake_thread.start()

    return 'Bot started', 200


@app.route('/end')
def end():
    global messages_queue, can_start
    messages_queue.put_nowait('END')
    can_start = True
    return 'Bot stopped', 200



if __name__ == '__main__':
    app.run()