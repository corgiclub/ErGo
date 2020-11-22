import re

pat = 'av[1-9][0-9]*'
st = 'av12'

g = re.match(pat, st, flags=re.I)

print(g)
