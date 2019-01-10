import re

pattern = re.compile('\d')

m = pattern.search('one1two2three3four4five5')

print(m.group())
print(m.span())
