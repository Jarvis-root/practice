import xml.dom.minidom

# 读取xml
dom = xml.dom.minidom.parse('D:\Practice\TestDemo\info.xml')
content = dom.documentElement
print(content.nodeName)
print(content.nodeValue)
print(content.nodeType)
print('--------------')
tag = content.getElementsByTagName('item')[1]
print(tag.getAttribute('id'))  # 获取标签的属性值
print('--------------')
tag1 = content.getElementsByTagName('caption')[0]
print(tag1.firstChild.data)  # 获取标签对之间的数据
