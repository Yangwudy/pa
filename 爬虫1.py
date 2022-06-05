import requests
import time
from bs4 import BeautifulSoup
import json

def get_content(url):
    comments = []
    headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53',
    }
    r = requests.get(url, timeout=30,headers=headers)
    r.raise_for_status()  #如果网页状态码返回200，表示网页能正常访问，如果网页请求出错就不执行接下来的操作
    r.endcodding = 'utf-8'
    html = r.text
    try:
        s=json.loads(html) #将JSON字符串转换为Python字典
    except:
        print("jsonload error")
    
    num=len(s['data']['replies']) 
    for i in range(num):
        com=s['data']['replies'][i]
        Dict={} 
        Dict['Uname']=com['member']['uname'] 
        Dict['Like']=com['like'] 
        Dict['Content']=com['content']['message']
        Dict['Time']=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(com['ctime']))
        comments.append(Dict)

    return comments


def out(dict):

    with open('BiliBiliComments.txt', 'a+',encoding='utf-8') as f:
        for comment in dict:
            try:
                f.write('姓名：{}\t  点赞数：{}\t \n 评论内容：{}\t  评论时间：{}\t \n '.format(comment['Uname'], comment['Like'], comment['Content'], comment['Time']))
                f.write("-----------------\n")
            except:
                print("out error")
        print('当前页面保存完成')

if __name__ == '__main__':
    e=0
    page=1
    while e == 0 and page<=100 :
        url = "https://api.bilibili.com/x/v2/reply/main?next={}&type=1&oid=552309529&mode=3".format(str(page))
        try:
            content=get_content(url)
            print("page:",page)
            out(content)
            page=page+1
            if page%10 == 0:
                time.sleep(5)
        except:
            e=1
