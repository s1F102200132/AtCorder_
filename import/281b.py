#import re
#S = input()
#print("Yes" if re.match(r"^[A-Z][1-9][0-9]{5}[A-Z]$", S) else "No")s = input()
s = input()
flag = False
 
if len(s) == 8:
  flag = True
  if s[0] < 'A' or 'Z' < s[0]:
    flag = False
  if s[7] < 'A' or 'Z' < s[7]:
    flag = False
  if s[1] < '1' or '9' < s[1]:
    flag = False
  for c in s[2:7]:
    if c < '0'or '9' < c:
      flag = False
      
print('Yes' if flag else 'No')