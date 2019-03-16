from itertools import groupby

def describe(numstr):
    s = ''
    for item in [''.join(v) for _, v in groupby(numstr)]:
        s += str(len(item)) + item[0]
    return s

numstr = '1'
for i in list(range(30)):
    numstr = describe(numstr)
print(len(numstr))
