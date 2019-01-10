import requests
# ssion = requests.session()
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
#
# data = {"email":"lewdster@163.com", "password":"!!!liu560"}
#
# ssion.post("http://www.renren.com/PLogin.do", data = data)
#
# resposne = ssion.get('http://www.renren.com/283455553')
#
# # print(resposne.text)



import requests
response = requests.get("https://www.12306.cn/mormhweb/",verify = False)
print(response.text)



