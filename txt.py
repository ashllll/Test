# coding:utf-8
txt = input("txt文件：")
with open(txt, "r") as f:  #打开文件
    data = f.read()  #读取文件
    print(data,'请确认文件是否正确！')
f.close()

