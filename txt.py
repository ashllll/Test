# coding:utf-8
txt = input("txt文件：")
with open(txt, "r") as f:  #打开文件
    data = f.read()  #读取文件
    print(data,'请确认文件是否正确！')
f.close()

import json

def insert_enter_after_postblend(value):
    if isinstance(value, dict):
        return {k: insert_enter_after_postblend(v) for k, v in value.items()}
    elif isinstance(value, list):
        return [insert_enter_after_postblend(item) for item in value]
    elif isinstance(value, str):
        return value.replace('"PostBlend', '"\nPostBlend')
    else:
        return value

def process_json_file(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # 应用函数
    data = insert_enter_after_postblend(data)

    # 保存修改后的JSON
    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
        print("处理完成!")


# JSON文件的路径
json_file_path = input("拖入文件:")

process_json_file(json_file_path)
