#-*- coding:utf-8 -*-
#学习测试Beautiful Soup4这个库，来解析访问html
from bs4 import BeautifulSoup

#创建一个html对象
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

#创建Bs对象
soup = BeautifulSoup(html, "html.parser")

#print(soup.prettify())

print(soup.title)
print(soup.a)
#打印类型
print(type(soup.a))
print(soup.a.name)
print(soup.a.attrs)
print(soup.a['class'])
#还可以对属性内容进行修改
soup.a['class'] = 'brother'
print(soup.a)
print(soup.a.string)
print(type(soup.a.string))

#可以获取标签内部的文字
print(soup.p)
print(soup.p.string)
print(type(soup.p.string))

#遍历文档书
print(soup.p.contents)
print("\n #############")
print(type(soup.body))
for child in  soup.body.children:
    print(type(child))
    print(child)

# 遍历所有子孙节点
print("\n *******************")
i = 0
for child in soup.descendants:
    i = i + 1
    print(str(i)+ "  ",child)

# 遍历多个内容
#for string in soup.strings:
#    print(repr(string))

#过滤掉空白内容
#for string in soup.stripped_strings:
#    print(repr(string))

#父节点
#print(soup.title.parent)

"""
content = soup.head.title.string
for parent in  content.parents:
    print(parent.name)
   # print(parent.attrs)
"""
print(soup.find_all('b'))

import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)