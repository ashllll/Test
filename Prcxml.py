# coding=utf-8
import os
import os.path
import xml.dom.minidom

"""修改xml路径"""


def path_1(FindPath, name1, file_name):  # 获取文件夹地址,name1:标签名
    if not os.path.isdir(file_name):  # 判断是否是文件夹,不是文件夹才打开
        print(file_name)  # 打印獲取文件名
        # 读取xml文件
        dom = xml.dom.minidom.parse(os.path.join(FindPath, file_name))  # 解析dom节点
        root = dom.documentElement
        label = root.getElementsByTagName(name1)  # 标签列表
        return dom, label


def xiugai_path(label):
    for i in range(len(label)):  # 遍歷文件列表長度
        print("打印所有路径", label[i].firstChild.data)  # 打印所有路径
        if label[i].firstChild.data[0:62] == "/home/hanqing/SSD-Tensorflow-master/VOC2019/JPEGImages/phone/":
            # print("/home/hanqing/SSD-Tensorflow-master/VOC2019/JPEGImages/phone/" + path_1[i].firstChild.data[
            #                                                                          62:-3] + "jpg", 1111111111)
            # 从新赋值
            label[i].firstChild.data = "/home/hanqing/SSD-Tensorflow-master/VOC2019/JPEGImages/phone/" + label[
                                                                                                             i].firstChild.data[
                                                                                                         62:-3] + "jpg"
        elif label[i].firstChild.data[:28] == "E:\my_own_search\phone\step1":
            # print("/home/hanqing/SSD-Tensorflow-master/VOC2019/JPEGImages/phone/" + path_1[i].firstChild.data[29:],
            #       22222222222222)
            # 从新赋值
            label[i].firstChild.data = "/home/hanqing/SSD-Tensorflow-master/VOC2019/JPEGImages/phone/" + label[
                                                                                                             i].firstChild.data[
                                                                                                         29:]
        elif label[i].firstChild.data.split(".")[1] != "jpg":  # 判断图片后缀是否是jpg
            label[i].firstChild.data = label[i].firstChild.data.split(".")[0] + ".jpg"
            # print("ok,地址：{}".format(label[i].firstChild.data))
        else:
            # print("可能需要修改值，如：后缀等",label[i].firstChild.data)
            print(None)
    return len(label)


# 修改neme
def xiugai_name(label, t_name=None):
    a, b = 0, 0
    c = 0
    for i in range(len(label)):
        c += 1
        print("打印所有name", label[i].firstChild.data, "一个XML有几个name：", c)
        if label[i].firstChild.data == "camera":  # 判断name是否camera，是修改，不是往下执行
            if t_name:
                label[i].firstChild.data = "camera1"
            a += 1  # 为镜头
        elif label[i].firstChild.data == "0":
            label[i].firstChild.data = "phone"  # 从新赋值
            b += 1  # 为手机
        else:
            print(label[i].firstChild.data)  # 不是上面两种是那种？看看
    return a, b


# 将修改后的xml文件保存
def baocun(xml_path, dom, file_name):  # 傳入保存文件路徑和文件名
    with open(os.path.join(xml_path, file_name), 'w') as fh:
        dom.writexml(fh)
        print('写入{}/pose OK!'.format(file_name[0:-4]))


if __name__ == "__main__":
    # 获得文件夹中所有文件
    FindPath = '/media/hanqing/AI开发/mubiaojiance/sj1'
    # 要保存地址
    xml_path = '/media/hanqing/AI开发/mubiaojiance/sj1'
    data = "name"  # 需要修改标签name
    a, b = 0, 0
    FileNames = os.listdir(FindPath)  # 獲取文件内容列表
    print(len(FileNames))
    for file_name in FileNames:  # 循環讀取文件名
        # print(file_name)#XML打印文件名
        list_1 = path_1(FindPath, data, file_name)
        c = xiugai_name(list_1[1], 1)  ##修改xml的name
        # print(c)
        # a+=c[0]#标签name数量
        # b+=c[1]#文件数量
        # xiugai_path(list_1[1])  # 1/解开注释修改路径方法
        baocun(xml_path, list_1[0], file_name)  # 2/保存数据
    # print("镜头数量为：{}".format(a),"手机标签数量为:{}".format(b),"xml总数：{}".format(len(FileNames)))

    # s = []
    # a,b,c=0,0,0
    # for file_name in list_1[1]:
    #     print(file_name)
    #     if not os.path.isdir(file_name):  # 判断是否是文件夹,不是文件夹才打开
    #         print(file_name)#打印獲取文件名
    # 读取xml文件
    # print(os.path.join(FindPath,file_name))#打印獲取文件路徑
    # dom = xml.dom.minidom.parse(os.path.join(FindPath,file_name))
    # root = dom.documentElement

    # # 获取标签对name之间的值
    # name = root.getElementsByTagName('name')
    # #獲取標籤路徑path
    # path_1=root.getElementsByTagName('path')

    # print(len(name))
    # for i in range(len(path_1)):#遍歷文件列表長度
    #     #if name[i] .firstChild.data== 'screw cap':
    #     ##
    #     if path_1[i].firstChild.data[0:62]=="/home/hanqing/SSD-Tensorflow-master/VOC2019/Annotations/phone/":
    #         # print("/home/hanqing/SSD-Tensorflow-master/VOC2019/JPEGImages/phone/" + path_1[i].firstChild.data[
    #         #                                                                          62:-3] + "jpg", 1111111111)
    #         path_1[i].firstChild.data = "/home/hanqing/SSD-Tensorflow-master/VOC2019/JPEGImages/phone/"+path_1[i].firstChild.data[62:-3]+"jpg"
    #     elif path_1[i].firstChild.data[:28]=="E:\my_own_search\phone\step1":
    #         # print("/home/hanqing/SSD-Tensorflow-master/VOC2019/JPEGImages/phone/" + path_1[i].firstChild.data[29:],
    #         #       22222222222222)
    #         path_1[i].firstChild.data ="/home/hanqing/SSD-Tensorflow-master/VOC2019/JPEGImages/phone/"+path_1[i].firstChild.data[29:]
    # print(len(path_1[i].firstChild.data))#長度
    # print(path_1[i].firstChild.data)
    # path_1[i].firstChild.data =path_1[i].firstChild.data#name[i].firstChild.data
    # print ('修改后的 path')
    # print (path_1[i].firstChild.data)
    # print(len("/home/hanqing/SSD-Tensorflow-master/VOC2019/Annotations/"))
    # c+=1
    # if name[i].firstChild.data=="phone":
    #     a+=1
    # else:
    #     b+=1
    # print(a,b,a+b,c)

    ##将修改后的xml文件保存
    # with open(os.path.join(xml_path, file_name), 'w') as fh:
    #     dom.writexml(fh)
    #     print('写入name/pose OK!')