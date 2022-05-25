import requests
import time
from bs4 import BeautifulSoup
import json

def get_html(url):
    headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53',
    }

    r = requests.get(url, timeout=30,headers=headers)
    r.raise_for_status()
    r.endcodding = 'utf-8'
    return r.text


def get_content(url):
    
    comments = []
    html = get_html(url)
    try:
        s=json.loads(html)
    except:
        print("jsonload error")
    
    num=len(s['data']['replies'])
    i=0
    while i<num:
        comment=s['data']['replies'][i]# 获取每栏评论

        InfoDict=comment['content']['message'] # 评论内容
        
        comments.append(InfoDict)
        i=i+1
    return comments


def Out2File(con):
    
    with open('BC.txt', 'a+',encoding='utf-8') as f:
        i=0
        for comment in con:
            i=i+1
            try:
                f.write(comment)
            except:
                print("out2File error")
        print('当前页面保存完成')

if __name__ == '__main__':
    e=0
    page=1
    while e == 0 and page<=20 :
        url = "https://api.bilibili.com/x/v2/reply/main?next={}&type=1&oid=552309529&mode=3".format(str(page))
        try:
            print()
            
            # print(url)
            content=get_content(url)
            print("page:",page)
            Out2File(content)
            page=page+1
        except:
            e=1
