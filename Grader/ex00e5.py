# 100
import re
n,m = input().split()
n = int(n)
m = int(m)

for i in range(2**n):
    if re.search('1{'+str(m)+',}', bin(i)[2:]):
        s = bin(i)[2:]
        print(s.zfill(n))