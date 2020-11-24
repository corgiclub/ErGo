import re

pat_aid = 'av[1-9][0-9]{0,8}'
pat_bid = 'bv[0-9a-z]{10}'
pat_srt = 'https://b23.tv/[0-9a-zA-z]{6}'

st = '3333av1223245'

g = re.search(pat_aid, st, flags=re.I)

print(g.group())

