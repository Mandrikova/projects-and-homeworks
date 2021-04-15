st = input()
letters = [[st[0], 1]]
for i in range(1, len(st)):
    f = True
    for item in range(len(letters)):
        if letters[item][0] == st[i]:
            letters[item][1] += 1
            f = False
    if f:
        letters.append([st[i], 1])
letters.sort(key=lambda x: x[1])

new = []
if len(letters) == 1:
    new.append([letters[0][0], 0])
else:
    while len(letters) > 1:
        a = letters[0]
        b = letters[1]
        letters.remove(a)
        letters.remove(b)
        letters.append([a[0]+b[0], a[1]+b[1]])
        letters.sort(key=lambda x: x[1])
        a[1] = 0
        b[1] = 1
        new.append(a)
        new.append(b)
    
d = {}
for i in range(len(new)-1, -1, -1):
    for s in new[i][0]:
        if s in d.keys():
            d[s] += str(new[i][1])
        else:
            d[s] = ''
            d[s] += str(new[i][1])

kod = ''
for s in st:
    kod += d[s]
print(len(d), ' ', len(kod))
for key in d:
    print("{}: {}".format(key, d[key]))
print(kod)