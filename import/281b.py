#import re
#S = input()
#print("Yes" if re.match(r"^[A-Z][1-9][0-9]{5}[A-Z]$", S) else "No")s = input()
s = input()
 
flag = True
if len(s) != 8:
    flag = False
if s[0].isalpha() == False or s[0] != s[0].upper():
    flag = False
if s[-1].isalpha() == False or s[-1] != s[-1].upper():
    flag = False
v = s[1:-1]
if v.isdigit() == False:
    flag = False
elif int(v) < 100000 or 999999 < int(v):
    flag = False
print('Yes' if flag else 'No')