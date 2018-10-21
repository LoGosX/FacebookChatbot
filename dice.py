import re
from random import randint
from personality import *

class RollADice(Personality):
    def onMessage(self, client, author_id, message_object, thread_id, thread_type, **kwargs):
        if not message_object.text:
            return
        pattern = r'^Roll a dice$'
        if re.match(pattern, message_object.text):
            client.send(Message("It's {}".format(randint(1,6))), thread_id=thread_id, thread_type=thread_type)
        pattern = r'^Roll range -?[0-9]+ -?[0-9]+$'
        s = re.match(pattern, message_object.text)
        if s:
            numbers = re.findall(r'-?[0-9]+',s.group())
            a = int(numbers[0])
            b = int(numbers[1])
            client.send(Message("It's {}".format(randint(min(a,b),max(a,b)))), thread_id=thread_id, thread_type=thread_type)
