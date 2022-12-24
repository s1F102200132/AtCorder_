import re
pattern = re.compile(r'[HDCS][A2-9TJQK]')
n = int(input())
strs = [input() for i in range(n)]
if any(not pattern.match(s) for s in strs):
    print("No")
else:
    print("Yes" if len(set(strs)) == n else "No")