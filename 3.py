import re
def us_to_bk(date):
    match = re.fullmatch('([0-9])[/]([0-9])[/]([0-9]{4})', date)
    return '{}/{}/{}'.format(match.group(2),match.group(1),match.group(3))
print(us_to_bk('9/4/2012'))