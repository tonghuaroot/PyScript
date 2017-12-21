#coding:utf8
#将str中的内容转为字符串，部分webshell采用此方式加密，方便解密
import re

str = """chr(102).chr(112)"""

new_str = str.split('.')

stri=''

for s in new_str:
    m = re.findall(r'(\w*[0-9]+)\w*',s)[0]
    a = chr(int(m))
    stri = stri+a
    print(stri)