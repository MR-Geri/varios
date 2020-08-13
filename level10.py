a = [1, 11, 21, 1211, 111221]
for _ in range(26):
    t = [[0, '0']]
    d = str(a[-1])
    for i in d:
        if t[-1][-1] == i:
            t[-1][0] += 1
        else:
            t.append([1, i])
    a.append(''.join([''.join([str(i[0]), str(i[1])]) for i in t[1:]]))
print(len(a[30]))
