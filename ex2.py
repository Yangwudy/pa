from aip import AipNlp
import jieba
APP_ID='26298747'
API_KEY = 'DAbtxtwPotKfeHhDfPWq7yFw'
SECRET_KEY = 'FmVMqjbUGcfMwq0bqS8jbNaQCdAQx4fd'
 
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
txt = open("BiliBiliComments.txt", "r", encoding="utf-8").read()
text=jieba.lcut(txt)
 
result=client.sentimentClassify(text)

items=result['items']
pos=items[0]['positive_prob']