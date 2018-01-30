
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""

"""
result = "These numbers could be telemarketers: \n"
excluded_calls = set([])
maybe_calls = []
for text in texts:
    excluded_calls.add(text[0])
    excluded_calls.add(text[1])

for call in calls:
    if call[0].startswith("140"):
        maybe_calls.append(call[0])
    if call[1].startswith("140"):
        excluded_calls.add(call[1])

result_calls = []
for call in maybe_calls:
    if call not in excluded_calls and call not in result_calls:
        result_calls.append(call)

result_calls.sort()
for call in result_calls:
    result += call + '\n'

print(result)