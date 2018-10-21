from personality import *

class KeepChatClean(Personality):
    def onMessage(self, client, author_id, message_object, thread_id, thread_type, **kwargs):
        
        messages = client.fetchThreadMessages(thread_id = thread_id, limit = 10, before = message_object.timestamp)
        if all(message.author == messages[0].author for message in messages):
            client.send(Message(text = 'Spamu nie tolerujemy'), thread_id=thread_id, thread_type=thread_type)
            client.removeUserFromGroup(messages[0].author, thread_id=thread_id)