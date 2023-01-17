import json
from string import ascii_lowercase
alphabet={}
for i in ascii_lowercase:
    alphabet[i] = ascii_lowercase.index(i)+1
#print(alphabet)
json_data = json.dumps(alphabet)
print(json_data)
