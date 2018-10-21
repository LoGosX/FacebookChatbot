import os
import time
from queue import Queue

from fbchat import Client, log
from fbchat.models import *

from choose_one import ChooseOne
from youtube_link import YoutubeLink
from stupid_reply import StupidReply
from dice import RollADice
from rip import Rip
from echo import Echo
from is_active import IsActive
from insult import Insult
from keep_chat_clean import KeepChatClean
from say_many_times import SayManyTimes
from post_meme import PostMeme
from image_rotater import RotateImage

class MyClient(Client):

    def __init__(self, email, password, queue, **kwargs):
        super(MyClient,self).__init__(email,password,**kwargs)
        self.onMessageListeners = set()
        self._start_time = time.time()
        self._IGNORE_TIME = 0
        self.queue = queue


    def onMessage(self, mid=None, author_id=None, message=None, message_object=None, thread_id=None, thread_type=ThreadType.USER, ts=None, metadata=None, msg=None):
        if not self.queue.empty():
            d = self.queue.get_nowait()
            if d == 'END':
                self.logout()
            self.queue.put_nowait(d)
        
        self.markAsDelivered(author_id, thread_id)
        self.markAsRead(author_id)
        if self._start_time and time.time() - self._start_time < self._IGNORE_TIME:
            return

        print('Got message:',message_object)
        for personality in self.onMessageListeners:
            try:
                personality.onMessage(client = self, mid=mid, author_id=author_id, message=message, message_object=message_object, thread_id=thread_id, thread_type=thread_type, ts=ts, metadata=metadata, msg=msg)
            except Exception as e:
                print(e)
                print('Occured in', personality)


def run(queue):
    while True:
        if not queue.empty():
            d = queue.get_nowait()
            if d == 'END':
                while not queue.empty():
                    queue.get_nowait()
                break

        try:
            email = os.environ['EMAIL']
            password = os.environ['PASSWORD']    
            client = MyClient(email,password,queue)
            client.onMessageListeners = set([RotateImage(), ChooseOne(), RollADice(), Echo(), Insult(), IsActive(), #KeepChatClean(), 
                Rip(), SayManyTimes(), StupidReply(), YoutubeLink(), PostMeme()])
            client.listen()
        except Exception as e:
            print(e)

    print('Finished')