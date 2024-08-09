import json



with open('tests.json', 'r', encoding='utf-8') as tf:
    data_test = json.load(tf)
    ty = data_test.readlines()
    with open('bufer.txt', 'w', encoding='utf-8') as bf:
        bf.write(ty)
    print(data_test)
    print(data_test['tests'])
    print(len(data_test['tests']))
    print(data_test['tests'][0])
    print(len(data_test['tests'][0]))
    print(data_test['tests'][1])
    print(len(data_test['tests'][1]))
    print(data_test['tests'][2])
    print(len(data_test['tests'][2]))
    print(data_test['tests'][3])
    print(len(data_test['tests'][3]))
with open('bufer.txt', 'w', encoding='utf-8') as bf:
    for i in data_test:
        bf.write(i)

with open('values.json', 'r', encoding='utf-8') as vf:
    data_values = json.load(vf)

list_of_values = []


def calc_id(data):
    if type(data) is dict:
        for keys, sub_list in data.items():
            if keys == 'value':
                if sub_list['value']:
                    list_of_values.append(sub_list['value'])
                    # print(f"печатаем словарь {list_of_values}")
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
                        # print(f"печатаем список {list_of_values}")
                        # print(f"что-то там со списком {data}")
                    elif keys == 'values':
                        calc_id(i[keys])
            else:
                calc_id(i)


calc_id(data_values)


def new_func():
    pass





# def replace(data, lv, count):
#     if type(data) is dict:
#         for keys, sub_list in data.items():
#             if keys == 'value':
#                 print(f"count for dict {count}")
#                 data[keys] = lv[count]
#                 count += 1
#                 print(f"печатаем словарь {lv} {count}")
#             elif keys == 'values':
#                 replace(data[keys], lv, count)
#     elif type(data) is list:
#         for i in data:
#             if type(i) is dict:
#                 for keys, sub_list in i.items():
#                     if keys == 'value':
#                         print(f"count for list {count}")
#                         i['value'] = list_of_values[count]
#                         count += 1
#                         print(f"печатаем список {list_of_values} {count}")
#                         # print(f"что-то там со списком {data}")
#                     elif keys == 'values':
#                         replace(i[keys], lv, count)
#             else:
#                 replace(i, lv, count)
#
#
#
#
# with open('rezult.json', 'w', encoding='utf-8') as rf:
#     json.dump(replace(data_test["tests"], list_of_values, 0), rf, indent=2)
#
#


# def replace(data, lv, count):
#     for j in range(len(data)):
#         if type(data) is dict:
#             for keys, sub_list in data.items():
#                 if keys == 'value':
#                     print(f"count for dict {count}")
#                     data[keys] = lv[count]
#                     count += 1
#                     print(f"печатаем словарь {lv} {count}")
#                 elif keys == 'values':
#                     replace(data[keys], lv, count)
#         elif type(data) is list:
#             for i in data:
#                 if type(i) is dict:
#                     for keys, sub_list in i.items():
#                         if keys == 'value':
#                             print(f"count for list {count}")
#                             i['value'] = list_of_values[count]
#                             count += 1
#                             print(f"печатаем список {list_of_values} {count}")
#                             # print(f"что-то там со списком {data}")
#                         elif keys == 'values':
#                             replace(i[keys], lv, count)
#                 else:
#                     replace(i, lv, count)
#         if count < len(list_of_values):
#             replace(data_test["tests"][3], lv, count)
#         elif count < len(list_of_values)
#             break
#
#
# with open('rezult.json', 'w', encoding='utf-8') as rf:
#     json.dump(replace(data_test["tests"], list_of_values, 0), rf, indent=2)


# with open('tests.json', 'r', encoding='utf-8') as tf:
#     with open('tests.json', 'w', encoding='utf-8') as tf1:
#         a = tf.readlines()
#         json.dump(a, tf1)



# with open('report.json', 'w', encoding='utf-8') as rf:
#     with open('tests.json', 'r', encoding='utf-8') as tf:
#         a = tf.readlines()
#         json.dump(a, rf.rstrip('\n'))


# def write_report(list_of_values, data):
#     rezult = {}
#     count = 0
#     if type(data) is dict:
#         for keys, volume in data.items():
#             if keys == 'value':
#                 rezult['value'] = list_of_values[count]
#                 count += 1
#             else:
#                 rezult.setdefault(data[keys], data[volume])
#     elif type(data) is list:
#         for i in data:
#             if type(i) is dict:
#                 for an_keys, sub_list in i.items():
#                     if an_keys == 'value':
#                         rezult['value'] = list_of_values[count]
#                         count += 1
#                     else:
#                         rezult.setdefault(data[an_keys], data[sub_list])
#             else:
#                 write_report(i)


# rezult = {}
# with open('report.json', 'w+r', encoding='utf-8') as rf:
#     for keys, values in data.items():
#         if data['id'] ==
#         if keys == 'value':
#             rf.write(rezult.setdefault(data['id'], data['value']))
#             print(f"печатаем список {rezult}")
#             print(f"что-то там со списком {data}")
#         else:
#             rf.write(rezult.setdefault(data[keys], data[values]))
#     data_test


# write_report(data_values, data_test)


# print(data1[0]['value'])

# with open('values.json', 'r', encoding='utf-8') as vf:
#     data2 = json.load(vf)
# print(data2)


# def find_in_list_of_list(data):
#     char = 'value'
#     for sub_list in data:
#         if char in sub_list:
#             return (data.index(sub_list), sub_list.index(char))
#     raise ValueError(f"'{char}' is not in list")
#
#
# find_in_list_of_list(data1)
