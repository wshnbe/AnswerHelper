#!/usr/bin/env python
# _*_ coding:utf-8 _*_

'this is a test for str count()'

import solve_utils as su 

que = '影片《心花路放》周冬雨饰演什么角色'
answer = ['洗头妹','按摩女','洗脚妹']

c = su.words_count(que,answer)
s = su.search_count(que,answer)
print(c)
print(s)