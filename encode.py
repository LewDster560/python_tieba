import urllib.parse

word = {'学校': '太工'}

good = urllib.parse.urlencode(word)

print(good)
print(urllib.parse.unquote(good))
