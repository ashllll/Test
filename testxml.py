# coding:utf-8
# https://codeantenna.com/a/3F24HagWPR 来源
import os
import os.path
import xml.dom.minidom

# path="../xml/"
path = input("指纹蒙版文件路径：")
txt = input("生成的XTX文件：")
with open(txt, "r") as f:  #打开文件
    data = f.read()  #读取文件
    print(data,'请确认文件是否正确！')
f.close()
#'''/home/kanghao/learning_something/about_xml/xml/' #Mac与Win反斜线定义不一样，开发环境为Mac，Win上注意替换为"\"'''
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

        ###获取标签对brightness之间的值
        brightness = root.getElementsByTagName('brightness')
        #ymin = root.getElementsByTagName('ymin')

        # 修改相应标签的值
        for i in range(len(brightness)):
            print(brightness[i].firstChild.data)
            a = brightness[i].firstChild.data
            print(type(a))
            brightness[i].firstChild.data = data   # 替换的指纹蒙版数据，还未定义数据来源！！！
            print(brightness[i].firstChild.data)

        '''for j in range(len(ymin)):
            print
            ymin[j].firstChild.data
            ymin[j].firstChild.data = 100
            print
            ymin[j].firstChild.data'''

        # 保存修改到xml文件中
        with open(os.path.join(path, xmlFile), 'w') as fh:
            dom.writexml(fh)
            print('恭喜，写入指纹蒙版数据成功！')

#if __name__ == "__main__":
    # 要求改的指纹蒙版文件
    #path = input("请拖入UDFP:")
    #



