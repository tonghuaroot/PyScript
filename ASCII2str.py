#ASCII码转字符串
def ascii2stri(stri):
    stri=stri.split(',')
    new_stri=''
    for i in stri:
        new_stri = new_stri + chr(int(''.join(i)))
    return new_stri

#字符串转ASCII码
def stri2ascii(stri):
    stri=stri
    new_stri=''
    for i in stri:
        new_stri = new_stri+str(ord(i))+","
    return new_stri[:-1]
	
stri='test'
print(stri2ascii(stri))
