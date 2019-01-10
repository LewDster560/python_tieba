from urllib import request
import urllib.parse
import random

word = {'学校': '太工'}
my_key = urllib.parse.urlencode(word)

url = 'http://www.baidu.com/s?' + my_key
ua_list = [
    "Mozilla/5.0 (Windows NT 6.1; ) Apple.... ",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0)... ",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X.... ",
    "Mozilla/5.0 (Macintosh; Intel Mac OS... "
]

user_agent = random.choice(ua_list)

req = request.Request(url)
req.add_header("Connection", "keep-alive")
req.add_header('User-Agent', user_agent)

response = request.urlopen(req)
print(req.get_header('User-agent'))
print('=======================================================')pip install requests

print(response.code)
print(response.headers)
page = response.read()
print('=======================================================')
print(page)

http_handler = urllib.request.HTTPHandler()
opener = urllib.parse.build_operner(http_handler)
