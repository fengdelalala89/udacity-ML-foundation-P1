import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""

"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

"""
call_map = {}

for call in calls:
    if call[0] in call_map:
        call_map[call[0]] += int(call[-1])
    else:
        call_map[call[0]] = int(call[-1])

longest_call = {"telephone": 0, "total_time": 0}

for call in call_map:
    if call_map.get(call) > longest_call["total_time"]:
        longest_call["telephone"] = call
        longest_call["total_time"] = call_map.get(call)

result = "{} spent the longest time, {} seconds, on the phone during September 2016."\
    .format(longest_call["telephone"], longest_call["total_time"])

print(result)