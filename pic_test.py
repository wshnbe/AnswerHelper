#!/usr/bin/env python
# _*_ coding:utf-8 _*_

'this is a test for save picture'

from PIL import ImageGrab
from aip import AipOcr
import config

client = AipOcr(config.APP_ID, config.API_KEY, config.SECRET_KEY)

#box = (200, 400, 988, 1050)
#im = ImageGrab.grab(box)
#im.save("pic.png")

filePath = "tupian1.png"  
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
print(result)