# coding:utf-8

import os.path
import xml.dom.minidom

# path="../xml/"
path = input("UDFPXML:")
txt = input("txt文件：")
with open(txt, "r") as f:  #打开文件
    data = f.read()  #读取文件
    print(data,'请确认文件是否正确！')
f.close()

files = os.listdir(path)  # 得到文件夹下所有文件名称
s = []

for xmlFile in files:  # 遍历文件夹
    if not os.path.isdir(xmlFile):  # 判断是否是文件夹，不是文件夹才打开
        print(xmlFile)

        # xml读取操作

        # 将获取到的xml文件名送入到dom解析
        # 错误代码：dom=xml.dom.minidom.parse(xmlFile)
        dom = xml.dom.minidom.parse(os.path.join(path, xmlFile))
        root = dom.documentElement

        ###获取标签对xmin/ymin之间的值
        brightness = root.getElementsByTagName('brightness')

        # 修改相应标签的值
        for i in range(len(brightness)):
            print(brightness[i].firstChild.data)
            a = brightness[i].firstChild.data
            print(type(a))
            brightness[i].firstChild.data = 200
            print(brightness[i].firstChild.data)

        # 保存修改到xml文件中
        with open(os.path.join(path, xmlFile), 'w') as fh:
            dom.writexml(fh)
            print('恭喜，写入UDFP成功！')