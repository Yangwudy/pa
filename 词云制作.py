import jieba
from matplotlib.pyplot import imread
import wordcloud

txt = open("BiliBiliComments.txt", "r", encoding="utf-8").read()
mask = imread("dls.jpg") #设置背景图片
stopwords = set() 
content = [line.strip() for line in open('cn_stopwords.txt','r',encoding="utf-8").readlines()]
stopwords.update(content)  #设置停用词
w = wordcloud.WordCloud(stopwords=stopwords,mask=mask,font_path="msyh.ttc",background_color="white",collocations=False)
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("dls.png")