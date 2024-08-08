n = int(input())
s = str(n)
res = 0
for i in range(0,len(s)):
    res+=(ord(s[i])-48)
print(res)
