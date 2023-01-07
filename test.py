from collections import Counter

lines = []
with open('test.txt', 'r', encoding='gbk') as f:
    for line in f:
        start = line.find("'")
        end = line.find("'", start + 1)
        result = line[start:end + 1]
        result = result.replace("'", "")
        lines.append(result.strip())

counts = Counter(lines)
total=''

for value, count in counts.items():
    total = total + str(count)
print(total)

count1 = total.count("1")
count2 = total.count("2")
count3 = total.count("3")
count4 = total.count("4")
print(str(count1)+','+str(count2)+','+str(count3)+','+str(count4))



