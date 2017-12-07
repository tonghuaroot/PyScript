#以POST方式向Web服务器发包
#POST数据为json格式

import requests
import json

headers = {
'Host':'www.xxx.com',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0',
'Accept':'application/json, text/plain, */*',
'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Accept-Encoding':'gzip, deflate, br',
'Referer':'https://www.xxx.com/xxx',
'X-Requested-With':'XMLHttpRequest',
'Content-Type':'application/json;charset=utf-8',
'Content-Length':'274',
'Cookie':'xxx',
'Connection':'keep-alive'
}

payload = {
'nickname': "tonghua", 
'id_number': '4fb8ec19d385a15fb1dfe832ecffe1107a2c7a76453e', 
'phone':'7b2134deffc00d3b1516a',
'address':'asdasdasdas',
'action':'change'
}

url = "https://www.xxx.com/xxx/if_info"

r = requests.post(url, headers=headers, data=json.dumps(payload))

print(r.text)
