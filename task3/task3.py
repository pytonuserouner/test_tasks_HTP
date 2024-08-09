import json
import pandas as pd



df = pd.read_json("tests.json")
df.to_csv("bufer.txt", index=False)


with open('tests.json', 'r', encoding='utf-8') as tf:
    data_test = json.load(tf)

with open('values.json', 'r', encoding='utf-8') as vf:
    data_values = json.load(vf)

list_of_values = []


def calc_id(data):
    if type(data) is dict:
        for keys, sub_list in data.items():
            if keys == 'value':
                if sub_list['value']:
                    list_of_values.append(sub_list['value'])
                else:
                    calc_id(sub_list[keys])
            else:
                calc_id(data[keys])
    elif type(data) is list:
        for i in data:
            if type(i) is dict:
                for keys, sub_list in i.items():
                    if keys == 'value':
                        list_of_values.append(i['value'])
                    elif keys == 'values':
                        calc_id(i[keys])
            else:
                calc_id(i)

calc_id(data_values)

print(list_of_values)

count = 0


def replace(data, lv, count):
    if type(data) is dict:
        for keys, sub_list in data.items():
            if keys == 'value':
                print(f"count for dict {count}")
                data[keys] = lv[count]
                count += 1
                print(f"печатаем словарь {lv} {count}")
            elif keys == 'values':
                replace(data[keys], lv, count)
    elif type(data) is list:
        for i in data:
            if type(i) is dict:
                for keys, sub_list in i.items():
                    if keys == 'value':
                        print(f"count for list {count}")
                        i['value'] = list_of_values[count]
                        count += 1
                        print(f"печатаем список {list_of_values} {count}")
                        # print(f"что-то там со списком {data}")
                    elif keys == 'values':
                        replace(i[keys], lv, count)
            else:
                replace(i, lv, count)

replace(data_test['tests'], list_of_values, count)

