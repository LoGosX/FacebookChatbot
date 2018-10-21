from personality import *
import re
from random import choice

class ChooseOne(Personality):
    def onMessage (self, client, author_id, message_object, thread_id, thread_type, **kwargs):
        if not message_object.text:
            return
        pattern = r'Choose one: (.+,)?.+'
        result = re.match(pattern,message_object.text)
        if result:
            options = result.group()[12:].split(',')
            client.send(Message(choice(options)), thread_id=thread_id, thread_type=thread_type)