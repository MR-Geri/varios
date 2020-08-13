import zipfile


name = '90052'
list_com = []
list_fi = []
with zipfile.ZipFile('channel.zip') as zip:
    for num in range(len(zip.infolist()) - 1):
        list_com.append(zip.getinfo(str(name) + ".txt").comment.decode('utf-8'))
        with zip.open(str(name) + ".txt") as act:
            name = str(str(act.read()).split()[-1][:-1])
print(''.join(list_com))
