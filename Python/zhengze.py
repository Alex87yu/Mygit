import re
s="ali ABROAD ROAD"
print(s)
#re.sub(r'\bROAD\b',"RD.",s)
s.replace('ROAD',"RD.")
print(s)
re.sub(r'\bROAD\b', 'RD.', s)
print(s)
re.sub(r'\bROAD', 'RD.', s)
print(s)


