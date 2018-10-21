from personality import *
import re
from random import choice

insults = [
'Ale masz ryj kto ci tak narysował?',

'Wyglądasz jak przez okno',

'Podniecasz się tym jak kura miesiączką',

'Nie przychodź do mnie do domu bo mi pies ucieknie',

'Masz twarz jakby cię w dzieciństwie karmili z procy',

'Nie mów do mnie bo twój oddech gniecie mi koszule',

'Daj mi swoje zdjęcie, bo mi krowa nie chce zdechnąć',

'Masz nawalone jak cyganka w tobołku',

'Masz szczęście, ze ślepy ciebie nie widzi',

'Masz gębę jak tłuczek do ziemniaków',

'Jesteś rozwinięty jak papier toaletowy',

'Wyrobiłeś się jak gumka w gaciach',

'Masz łeb z tego materiału co kangur torbę !',

'Wyciśnij tego pryszcza ,może ci głowa urośnie',

'Masz oczy jak wejście AUDIO-VIDEO',
]

class Insult(Personality):
    def onMessage(self, client, author_id, message_object, thread_id, thread_type, **kwargs):
        if not message_object.text:
            return
        pattern = r'^Insult @(\w+ \w*)'
        result = re.match(pattern,message_object.text)
        if result:
            client.send(Message(text = '{} {}'.format(result.group(1), choice(insults))), thread_id=thread_id, thread_type=thread_type)