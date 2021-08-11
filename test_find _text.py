import re

s= 'this is a pen  pan pain'


l=re.findall('[^p.n]',s)
print(l)