import requests

# response = requests.post('http://www.baidu.com')
#
# print(response.text)


response = requests.get("http://www.baidu.com")
cookiesjar = response.cookies
print(cookiesjar)

cookiesdict = requests.utils.dict_from_cookiejar(cookiesjar)
print(cookiesdict)

# print(response.text)







