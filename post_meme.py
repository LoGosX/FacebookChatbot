from personality import *

from random import choice

memes = [
    #'https://img-9gag-fun.9cache.com/photo/anMeQwb_460sv.mp4',
    #'https://img-9gag-fun.9cache.com/photo/aDzbrPB_460sv.mp4',
    #'https://img-9gag-fun.9cache.com/photo/anbwppL_460sv.mp4',
    #'https://img-9gag-fun.9cache.com/photo/a6bgGb9_460sv.mp4',
    #'https://img-9gag-fun.9cache.com/photo/axVQ0zL_460sv.mp4',
    #'https://img-9gag-fun.9cache.com/photo/a9rmeLD_460sv.mp4',
    #'https://img-9gag-fun.9cache.com/photo/aBW8711_460sv.mp4',
    'https://img-9gag-fun.9cache.com/photo/axGV9W2_460s_v1.jpg',
    'https://img-9gag-fun.9cache.com/photo/a3MVdg5_460s.jpg',
    'https://img-9gag-fun.9cache.com/photo/ax05LP1_460s.jpg',
    'https://img-9gag-fun.9cache.com/photo/aNz722v_460s.jpg',
    'https://img-9gag-fun.9cache.com/photo/awQDxyB_460s.jpg',
    'https://img-9gag-fun.9cache.com/photo/a5nvmpG_460s.jpg',
    'https://img-9gag-fun.9cache.com/photo/apQjqN8_460s.jpg',
    'https://img-9gag-fun.9cache.com/photo/a1KOxPv_460s.jpg',
    'https://img-9gag-fun.9cache.com/photo/apQg2r9_460s.jpg',
    'https://img-9gag-fun.9cache.com/photo/a1K1bw6_460s.jpg',
    'https://img-9gag-fun.9cache.com/photo/awQrBjQ_460s.jpg',
    'https://img-9gag-fun.9cache.com/photo/ad9yvbQ_460s.jpg',
    'https://img-9gag-fun.9cache.com/photo/agLRyx6_460s.jpg',
    'https://img-9gag-fun.9cache.com/photo/aEYLp8x_460s.jpg',
    'https://img-9gag-fun.9cache.com/photo/appZY7E_460s_v1.jpg',
    'https://img-9gag-fun.9cache.com/photo/aNA7Zb4_460s.jpg',
    'https://img-9gag-fun.9cache.com/photo/a3qX04e_460s.jpg',
    'https://img-9gag-fun.9cache.com/photo/aDWv9dx_460s.jpg',
    'https://img-9gag-fun.9cache.com/photo/a1bnjE6_460s.jpg',
    'https://img-9gag-fun.9cache.com/photo/aOzODN2_460s.jpg',
    'https://img-9gag-fun.9cache.com/photo/amYOBgV_460s.jpg',
    'https://img-9gag-fun.9cache.com/photo/aeb7g75_460s.jpg',
    'https://img-9gag-fun.9cache.com/photo/a6bN7bL_460s.jpg',
    'https://img-9gag-fun.9cache.com/photo/a9rpjp0_460s.jpg',
    'https://img-9gag-fun.9cache.com/photo/ad777ED_460s.jpg',
    'https://img-9gag-fun.9cache.com/photo/a2rmn2e_460s.jpg',
    'https://img-9gag-fun.9cache.com/photo/aDWoKXN_460s.jpg',
    'https://img-9gag-fun.9cache.com/photo/aYxe3O0_460s.jpg',
    'https://img-9gag-fun.9cache.com/photo/aAd1p30_460s.jpg',
    'https://img-9gag-fun.9cache.com/photo/aEYvvLN_460s.jpg',
    ['https://img-9gag-fun.9cache.com/photo/awQpDPW_460s.jpg',
    'https://img-9gag-fun.9cache.com/photo/aNzbX8b_460s.jpg'],
    ['https://img-9gag-fun.9cache.com/photo/aEBbOgG_460s.jpg',
    'https://img-9gag-fun.9cache.com/photo/apQXY5p_460s.jpg'],
]

class PostMeme(Personality):
    def onMessage(self, client, author_id, message_object, thread_id, thread_type, **kwargs):
        if not message_object.text:
            return
        if message_object.text == 'Meme':
            meme = choice(memes)
            if isinstance(meme,str):
                client.sendRemoteImage(meme, message=None, thread_id=thread_id, thread_type=thread_type)
            else:
                for mem in meme:
                    client.sendRemoteImage(mem, message=None, thread_id=thread_id, thread_type=thread_type)