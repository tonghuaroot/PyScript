# 将Unicode编码的字符串转换为中文
from optparse import OptionParser

usage = "Unicode2Chinese.py [-u <string>]"
parser = OptionParser()

parser.add_option("-u", "--unicode", action="store", type="string", dest="unicode_str", help="将Unicode编码的字符串转换为中文")
(options, args) = parser.parse_args()
chinese = options.unicode_str.encode('utf-8').decode('unicode_escape')
print(chinese)
