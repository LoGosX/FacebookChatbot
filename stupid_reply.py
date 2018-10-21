import re
from random import randint
from personality import *
from functools import reduce

class StupidReply(Personality):
    def onMessage(self, client, author_id, message_object, thread_id, thread_type, **kwargs):
        if not message_object.text:
            return
        pattern = r'^".{,}"$'
        if re.match(pattern, message_object.text):
            new_text = reduce(lambda y,x: y + (x.upper() if randint(0,1) == 0 else x.lower()), message_object.text[1:-1]) 
            client.send(Message(new_text), thread_id=thread_id, thread_type=thread_type)