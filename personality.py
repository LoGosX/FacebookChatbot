from fbchat import Client, log
from fbchat.models import *

class Personality:
    
    def onMessage(self,client, mid=None, author_id=None, message=None, message_object=None, thread_id=None, thread_type=ThreadType.USER, ts=None, metadata=None, msg=None):
        """
        Called when the client is listening, and somebody sends a message
        :param mid: The message ID
        :param author_id: The ID of the author
        :param message: (deprecated. Use `message_object.text` instead)
        :param message_object: The message (As a `Message` object)
        :param thread_id: Thread ID that the message was sent to. See :ref:`intro_threads`
        :param thread_type: Type of thread that the message was sent to. See :ref:`intro_threads`
        :param ts: The timestamp of the message
        :param metadata: Extra metadata about the message
        :param msg: A full set of the data recieved
        :type message_object: models.Message
        :type thread_type: models.ThreadType
        """
        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))