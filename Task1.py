import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
"There are <count> different telephone numbers in the records."
"""
phone_set = set([])

for text in texts:
    phone_set.add(text[0])
    phone_set.add(text[1])

for call in calls:
    phone_set.add(call[0])
    phone_set.add(call[1])

result = "There are {} different telephone numbers in the records.".format(len(phone_set))
print(result)
