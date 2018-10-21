import os
import sys
import json
import threading
from queue import Queue

from flask import Flask, request

from my_client import run

app = Flask(__name__)

messages_queue = Queue()

main_thread = None

can_start = True

@app.route('/')
def webhook():
    return 'Okey', 200

@app.route('/start')
def start():
    global main_thread, messages_queue, can_start
    if can_start:
        main_thread = threading.Thread(target=run, args=(messages_queue,))
        main_thread.start()
        can_start = False
    
    return 'Bot started', 200


@app.route('/end')
def end():
    global messages_queue, can_start
    messages_queue.put_nowait('END')
    can_start = True
    return 'Bot stopped', 200



if __name__ == '__main__':
    app.run()