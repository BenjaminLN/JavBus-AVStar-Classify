# -*- coding: UTF8 -*-
import win32clipboard as wc
import win32con
from requests import Session
from bs4 import BeautifulSoup
from requests import utils
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

headers = {'User-Agent': 'Mozilla/5.0',}
cookiesDit = {'existmag':'all'}
url='https://www.javbus.com/star/nyi'
flag=1
result_list=[]

if url[-1]!='/':
    url=url+'/'

while True:
    request = Session()
    request.proxies = {"https": 'http://127.0.0.1:1080/pac?auth=6sZoXM8Q3lZyeXZMnVP-&t=201909182318551455'}
    res=request.get(url+str(flag),headers=headers,cookies=cookiesDit)
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
            result_list.append(fanhao)
            result_list.append(fanhao2)
    res.close()
    flag+=1
print('共',str(len(result_list)/2)[:-2],'部影片:')
result_list='|'.join(result_list)
print(result_list)
setCopy(result_list)
