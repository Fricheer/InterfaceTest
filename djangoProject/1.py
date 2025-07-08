lis = ' 123 456 789 '
lists = lis.split()
print(lists)
print(len(lists[-1]))

m = 1
n = len(lis)
s = 1
l = []
for i in lis:
    if i == ' ':
        l.append(s)
    else:
        pass
    if s < n:
        s += 1
    else:
        pass
num = l[-1] - l[-2] - 1
print(num)

def Convert(string):
    li = list(string.split())
    return li
print(Convert(lis))