from personality import *
from fbchat import Client, log
from fbchat.models import *

class Echo(Personality):
    def onMessage(self, client, author_id, message_object, thread_id, thread_type, **kwargs):
        if not message_object.text:
            return
        if author_id == client.uid:
            return
        if message_object.text.startswith('echo '):
            client.send(Message(text = message_object.text[5:]), thread_id=thread_id, thread_type=thread_type)