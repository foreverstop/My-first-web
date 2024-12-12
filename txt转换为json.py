import json

# 读取文本文件
with open('d:\\大三上学习文件\\网络GIS\\5\\hbcity.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 处理数据
data_list = []
headers = lines[0].strip().split(',')

for line in lines[1:]:
    if line.strip():  # 检查是否为空行
        values = line.strip().split(',')
        # 清理键并创建字典
        data_dict = {header.strip().replace('\ufeff', ''): value.strip() for header, value in zip(headers, values)}
        data_list.append(data_dict)

# 写入JSON文件
with open('d:\\大三上学习文件\\网络GIS\\实习\\hbcity.json', 'w', encoding='utf-8') as json_file:
    json.dump(data_list, json_file, ensure_ascii=False, indent=4)

print("转换完成，已生成 hbcity.json 文件。")

