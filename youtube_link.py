import re
import urllib.request
import urllib.parse
from personality import *

class YoutubeLink(Personality):
        def onMessage(self, client, author_id, message_object, thread_id, thread_type, **kwargs):
                if not message_object.text:
                        return
                if author_id == client.uid:
                        return
                pattern = r'^;Youtube: .{,};$'
                a = re.search(pattern,message_object.text)
                if a:
                    search_text = a.group()[10:len(a.group())-1]
                    query_string = urllib.parse.urlencode({"search_query" : search_text})
                    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
                    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
                    link = "http://www.youtube.com/watch?v=" + search_results[0]
                    client.send(Message(text = link), thread_id=thread_id, thread_type=thread_type)