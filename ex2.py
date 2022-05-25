from aip import AipNlp
import matplotlib.pyplot as plt
 
APP_ID='26298747'
API_KEY = 'DAbtxtwPotKfeHhDfPWq7yFw'
SECRET_KEY = 'FmVMqjbUGcfMwq0bqS8jbNaQCdAQx4fd'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
txt = open("BC.txt", "r", encoding="utf-8").read()
m=int(len(txt)/500)
txt=list(txt)
for i in range(1,m):
    txt.insert(i*500,'#')
txt=''.join(txt)
x=txt.split('#')
pos=0
neg=0
con=0
m=0

for i in range(59):
    try:
        result=client.sentimentClassify(x[i])
    except:
        if result.__contains__('items'):
            items=result['items']
            pos+=items[0]['positive_prob']
            neg+=items[0]['negative_prob']
            con=items[0]['confidence']
            m+=1
    else:
        i+=1
con=con/m

plt.rcParams['font.sans-serif'] = 'simhei'
data = [pos, neg]
label = ['积极情绪', '消极情绪'] 
plt.pie(data, labels = label, autopct='%.2f%%')
plt.title('本分析置信度为{}'.format(con))
plt.show()
