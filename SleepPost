#以POST方式向Web服务器循环发包
#并且延时
import requests
import time

headers = {
'Host':'www.xxx.com',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0',
'Accept':'application/json, text/plain, */*',
'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Accept-Encoding':'gzip, deflate, br',
'Referer':'https://www.xxx.com/emailVerify.html',
'X-Requested-With':'XMLHttpRequest',
'Content-Type':'application/json;charset=utf-8',
'Content-Length':'0',
'Cookie':'xxx',
'Connection':'keep-alive'
}

url = "https://www.xxx.com/xxx/if_email_verify?email=xxx%40qq.com"

for i in range(1000):
    r = requests.post(url, headers=headers)
    print(r.text)
    time.sleep(80)
