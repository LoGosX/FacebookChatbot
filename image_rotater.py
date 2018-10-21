import urllib
from PIL import Image
from personality import *
import re
_IMAGE_FILE = 'image.png'

 
#taken from
#https://www.blog.pythonlibrary.org/2017/10/05/how-to-rotate-mirror-photos-with-python/
def rotate(image_path, degrees_to_rotate, saved_location):
    """
    Rotate the given photo the amount of given degreesk, show it and save it
 
    @param image_path: The path to the image to edit
    @param degrees_to_rotate: The number of degrees to rotate the image
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    rotated_image = image_obj.rotate(degrees_to_rotate)
    rotated_image.save(saved_location)

def download_image(image_url):
    image_path = urllib.request.urlretrieve(image_url, _IMAGE_FILE)[0]
    return image_path

def download_and_rotate(image_url, degrees_to_rotate):
    image = download_image(image_url)
    rotate(image, degrees_to_rotate, image)
    return image

class RotateImage(Personality):

    def __init__(self, *args, **kwargs):
        self._last_image = None
        return super().__init__(*args, **kwargs)

    def _handle_image(self, client, image_attachment):
        image_url = client.fetchImageUrl(image_attachment.uid)
        self._last_image = image_url

    def _send_last_image_rotated(self, client, thread_type, thread_id, degrees_to_rotate):
        image_path = download_and_rotate(self._last_image, degrees_to_rotate)
        client.sendLocalFiles(image_path, thread_id = thread_id, thread_type=thread_type)

    def onMessage(self, client, mid=None, author_id=None, message=None, message_object=None, thread_id=None, thread_type=ThreadType.USER, ts=None, metadata=None, msg=None):
        if author_id == client.uid:
            return
        for attachment in message_object.attachments:
            if isinstance(attachment, ImageAttachment):
                self._handle_image(client, attachment)
        if not message_object.text:
            return
        if message_object.text.startswith('Rotate') or message_object.text.startswith('rotate'):
            d = message_object.text.split(' ')
            if len(d) >= 2:
                d = d[1]
            else:
                return self._send_last_image_rotated(client, thread_type = thread_type, thread_id=thread_id, degrees_to_rotate = 90)
            if not self._last_image:
                client.send(Message(text='No image to rotate.'), thread_id = thread_id, thread_type = thread_type)
                return
            if d in ['left', 'Left']:
                degress = 90
            elif d in ['Right', 'right']:
                degress = 270
            else:
                degress = 270
            return self._send_last_image_rotated(client, thread_type = thread_type, thread_id=thread_id, degrees_to_rotate = degress)