import matplotlib.pyplot as plt
import requests
import json

idict = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    '男': 0,
    '女': 0,
    '保密': 0
}

def gethtml(url):
    headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53',
    }
    r = requests.get(url, timeout=30,headers=headers)
    r.raise_for_status()
    r.endcodding = 'utf-8'
    html=r.text
    try:
        Dict=json.loads(html)
    except:
        print("jsonload error")
    return Dict

def getcontent(Dict):
    #提取评论内容
    comments = []
    num=len(Dict['data']['replies'])
    for i in range(num):
        message=Dict['data']['replies'][i]['content']['message']
        comments.append(message)
    return comments


def out(con):
    #保存至文件
    with open('BC.txt', 'a+',encoding='utf-8') as f:
        for comment in con:
            try:
                f.write(comment)
            except:
                print("out error")
        print('当前页面保存完成')


def pub(Dict):
    #提取关键信息
    global idict
    num=len(Dict['data']['replies'])
    for i in range(num):
        level = Dict["data"]["replies"][i]['member']['level_info']["current_level"]
        sex = Dict["data"]["replies"][i]['member']['sex']
        idict[level]+=1
        idict[sex]+=1

if __name__ == '__main__':
    e=0
    page=1
    x=[]
    while e == 0 and page<=20:
        url = "https://api.bilibili.com/x/v2/reply/main?next={}&type=1&oid=552309529&mode=3".format(str(page))
        try:
            d=gethtml(url)
            #content=getcontent(d)
            print("page:",page)
            #out(content)
            pub(d)
            page=page+1
        except:
            e=1
            
    #进行数据分析       
    for i in range(1,7):
        x.append(idict[i])
    label = ['lv.1', 'lv.2','lv.3','lv.4','lv.5','lv.6'] 
    plt.pie(x, labels = label, autopct='%.2f%%')
    plt.title('评论用户等级分布')
    '''
    plt.rcParams['font.sans-serif'] = 'simhei'
    x=[idict['男'],idict['女'],idict['保密']]
    label = ['男', '女', '保密'] 
    plt.pie(x, labels = label, autopct='%.2f%%')
    plt.title('评论用户性别分布')
    '''
    plt.show()