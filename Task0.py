import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

first_text = texts[0]
result1 = "First record of texts, {} texts {} at time {}".format(first_text[0], first_text[1], first_text[2])

last_call = calls[-1]
result2 = "Last record of calls, {} calls {} at time {}, lasting {} seconds".format(last_call[0], last_call[1], last_call[2], last_call[3])
print(result1)
print(result2)
