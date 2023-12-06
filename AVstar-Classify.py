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

headers = {
        'accept-language': 'zh-CN,zh;q=0.9,zh-HK;q=0.8',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Chromium";v="117", "Not;A=Brand";v="8"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
    };
cookiesDit = {'existmag':'all'}
url='https://www.javbus.com/star/ytb'
flag=1
result_list=[]

if url[-1]!='/':
    url=url+'/'

while True:
    request = Session()
    request.proxies = {"https": '127.0.0.1:7890'}
    res=request.get(url+str(flag),headers=headers,cookies=cookiesDit)
    if res.status_code!=200:
        print(url + str(flag))
        break
    print(url+str(flag))
    res.content.decode("utf8","ignore").encode("gbk","ignore")

    soup=BeautifulSoup(res.text,'html.parser')
    # print(soup)
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
