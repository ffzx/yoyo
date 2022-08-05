"""
读取yaml 或json
"""
import yaml
import os
import json


def readyml(yml_path):
    """
    读取yaml文件内容，转成python字典或list
    """
    if not os.path.isfile(yml_path):
        raise FileNotFoundError(f"文件路径不存在，请检查路径是否正确：{yml_path}")
    f = open(yml_path, 'r', encoding='utf-8')
    res = f.read()
    f.close()
    # print(f"读取的数据格式：{res}")
    return yaml.safe_load(res)


def read_json(json_path):
    if not os.path.isfile(json_path):
        raise FileNotFoundError(f"文件路径不存在，请检查路径是否正确：{json_path}")
    fp = open(json_path, 'r', encoding='utf-8')
    return json.load(fp)


if __name__ == '__main__':
    r = readyml("data2.yml")
    print(r)
    r2 = read_json('data1.json')
    print(r2)

