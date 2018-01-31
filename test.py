#!/usr/bin/env python
#_*_ coding:utf-8 _*_

'this is for test'

from aip import AipOcr
from PIL import ImageGrab,Image
import matplotlib.pyplot as plt
import config
import json
import requests
import solve_utils as su

client = AipOcr(config.APP_ID, config.API_KEY, config.SECRET_KEY)

box = (250, 250, 980, 950)
im = ImageGrab.grab(box)
im.save("test.png")

filePath = config.IMAGE_PAGE 
def get_file_content(filePath):  
    with open(filePath, 'rb') as fp:  
        return fp.read()  
  
# 定义参数变量  
options = {  
  'detect_direction': 'true',  
  'language_type': 'CHN_ENG',  
}  
  
# 调用通用文字识别接口  
result = client.basicGeneral(get_file_content(filePath), options)  
words = result['words_result']
question = ''
answer = []
flag = 1

#问题
if len(words) == 3:
	question = words[0]['words']; 
elif len(words) == 4:
    question = words[0]['words'];
elif len(words) == 5:
    question = words[0]['words'] + words[1]['words'];
    flag = 2;
elif len(words) == 6:
	question = words[0]['words'] + words[1]['words'] + words[2]['words'];
	flag = 3;
question = question.replace("?","")
print("问题 ：%s"  % question)

#选项
for i in range(flag,len(words)):
    answer.append(words[i]['words'])
    print("选项" + str(i - flag + 1) + u" : " +answer[i - flag])
c_counts = su.words_count(question,answer)
s_counts = su.search_count(question,answer)
#req = requests.get(url='http://www.baidu.com/s', params={'wd': que +"%20"+answer})
#body = req.text
#start = body.find(u'百度为您找到相关结果约') + 11
#body = body[start:]
#end = body.find(u'个')
#num = body[:end]
#num = num.replace(',','')
#print(num)

#import requests
#from PIL import ImageGrab

#box = (200, 400, 988, 1050)
#im = ImageGrab.grab(box)
#im.show()
#que = '中华人民共和国首都'
#answer = ['北京','上海','石家庄']

#c = su.words_count(que,answer)
#s = su.search_count(que,answer)


