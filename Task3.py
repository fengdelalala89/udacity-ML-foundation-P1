
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
# part1
part1_result = "The numbers called by people in Bangalore have codes:\n"

call_map = {}
for call in calls:
    if call[0].startswith("(080)") and call[1] not in call_map:
        if call[1].startswith("("):
            end = call[1].index(")")
            call_map[call[1]] = call[1][1:end]
        elif call[1].startswith("7") or call[1].startswith("8") or call[1].startswith("9"):
            call_map[call[1]] = call[1][:4]

codes = []
for call in call_map:
    if call_map[call] not in codes:
        codes.append(call_map[call])

codes.sort()
for code in codes:
    part1_result += code + "\n"

print (part1_result)

# part2
part2_result = "{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
total = 0.0
target = 0.0
for call in calls:
    if call[0].startswith("(080)"):
        total += 1.0
        if call[1].startswith("(080)"):
            target += 1.0

part2_result = part2_result.format(str(round(target / total * 100, 2)))
print(part2_result)