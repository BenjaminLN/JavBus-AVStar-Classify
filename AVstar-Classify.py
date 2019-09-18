# -*- coding: UTF8 -*-
import win32clipboard as wc
import win32con
from requests import Session
from bs4 import BeautifulSoup

# 获取剪切板内容
def getCopy():
    wc.OpenClipboard()
    t = wc.GetClipboardData(win32con.CF_UNICODETEXT)
    wc.CloseClipboard()
    return t
# 写入剪切板内容
def setCopy(str):
    wc.OpenClipboard()
    wc.EmptyClipboard()
    wc.SetClipboardData(win32con.CF_UNICODETEXT, str)
    wc.CloseClipboard()


headers = {'User-Agent': 'Mozilla/5.0'}
url='https://www.javbus.com/star/tyv'

flag=1
list=[]

if url[-1]!='/':
    url=url+'/'

while True:
    request = Session()
    request.proxies = {"https": ""}
    res=request.get(url+str(flag),headers=headers)
    if res.status_code!=200:
        print(url + str(flag))
        break
    print(url+str(flag))
    res.content.decode("utf8","ignore").encode("gbk","ignore")

    soup=BeautifulSoup(res.text,'html.parser')
    myfanhao=soup.find_all('date')
    for each in enumerate(myfanhao):
        if (each[0]+1)%2==1:
            fanhao=str(each[1])[6:-7]
            fanhao2=''.join(fanhao.split('-'))
            list.append(fanhao)
            list.append(fanhao2)
    res.close()
    flag+=1

list='|'.join(list)
print(list)
setCopy(list)
