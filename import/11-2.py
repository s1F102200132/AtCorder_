import re
def tail_ing_to_ed(s):
    new_str = re.sub(r'ing$', 'ed',s)
    return new_str
print(tail_ing_to_ed('playing'))

S = 'naan'
new_str = S.replace('na','nya')
print(new_str)