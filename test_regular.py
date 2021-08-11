import re

s=(input('Enter a number: '))

l=re.findall('[0-5][0-9]|60',s)

print(l)

