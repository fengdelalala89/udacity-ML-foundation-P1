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
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电

请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""

"""
判断是否是目标电话，目标为疑似电话推销的电话号码
判别逻辑：
    这样的电话总是向其他人拨出电话，但从来不发短信、接收短信或是收到来电
    其中:已经确认的电话促销员的号码没有括号或空格 , 但以140开头. 例如: `1402316533`
"""
result = "These numbers could be telemarketers: \n"
# 排除的电话集合
excluded_calls = set([])
# 存在嫌疑的电话集合
maybe_calls = set([])
# texts中的号码为排除的集合
for text in texts:
    excluded_calls.add(text[0])
    excluded_calls.add(text[1])
# 将calls中所有主动拨打电话的号码加入，存在嫌疑的电话集合中，将所有被叫号码加入排除集合
for call in calls:
    maybe_calls.add(call[0])
    excluded_calls.add(call[1])
# 在嫌疑电话集合中排除不符合判别条件的号码
result_calls = []
for call in maybe_calls:
    if call not in excluded_calls:
        result_calls.append(call)
# 排序
result_calls.sort()
for call in result_calls:
    result += call + '\n'

print(result)