d1 = [{"name":"a","sal":123}, {"name":"b","sal":123}]
d1.append({"name":"c","sal":123})

total = 0
for i in d1:
    total += i['sal']

print(total)

