from personality import *

class IsActive(Personality):
    def onMessage(self, client, author_id, message_object, thread_id, thread_type, **kwargs):
        if not message_object.text:
            return
        if author_id == client.uid:
            return
        if message_object.text == '!isActive':
            client.send(Message(text = '👋', emoji_size = EmojiSize.SMALL), thread_id=thread_id, thread_type=thread_type)