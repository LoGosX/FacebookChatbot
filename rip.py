from personality import *

class Rip(Personality):
    def onMessage(self, client, message_object, thread_id, thread_type, **kwargs):
        if not message_object.text:
            return
        if '[*]' == message_object.text:
            client.sendRemoteImage('https://i.imgur.com/5q1cAMn.jpg', message=None, thread_id=thread_id, thread_type=thread_type)