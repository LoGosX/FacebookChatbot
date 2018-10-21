from personality import *
import re

class SayManyTimes(Personality):
    def onMessage(self, client, author_id, message_object, thread_id, thread_type, **kwargs):
        if not message_object.text:
            return
        pattern = r'Say ([0-9]+) times: (.*)'
        result = re.match(pattern,message_object.text)
        if result:
            try:
                times = int(result.group(1))
                sentence = result.group(2)
                for _ in range(min(10, times)):
                    client.send(Message(text = sentence), thread_id=thread_id, thread_type=thread_type)
            except Exception as e:
                message = f"""
                Exception occured: {e}\n
                Pattern is {pattern}
                """
                client.send(Message(text=message), thread_id=thread_id, thread_type=thread_type)
