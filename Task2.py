# -*- coding:utf-8 -*-
"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""
def cumulative(call_number, time, call_map):
    """
    按照电话号码，给电话字典累加时长
    :param call_number: 电话号码
    :param time:        通话时长
    :param call_map:    电话字典
    """
    if call_number in call_map:
        call_map[call_number] += int(time)
    else:
        call_map[call_number] = int(time)

call_map = {}

# 累加时长，接听电话的时间也是通话时间的一部分
for call in calls:
    cumulative(call[0], call[-1], call_map)
    cumulative(call[1], call[-1], call_map)

longest_call = {"telephone": 0, "total_time": 0}

for call in call_map:
    if call_map.get(call) > longest_call["total_time"]:
        longest_call["telephone"] = call
        longest_call["total_time"] = call_map.get(call)

result = "{} spent the longest time, {} seconds, on the phone during September 2016."\
    .format(longest_call["telephone"], longest_call["total_time"])

print(result)