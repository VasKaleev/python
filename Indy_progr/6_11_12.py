words = ['mention', 'soup', 'pneumonia', 'tradition', 'concert', 'tease', 'generation',
         'winter', 'national', 'jacket', 'winter', 'wrestle', 'proposal', 'error', 
         'pneumonia', 'concert', 'value', 'value', 'disclose', 'glasses', 'tank',
         'national', 'soup', 'feel', 'few', 'concert', 'wrestle', 'proposal', 'soup',
         'sail', 'brown', 'service', 'proposal', 'winter', 'jacket', 'mention', 'tradition',
         'value', 'feel', 'bear', 'few', 'value', 'winter', 'proposal', 'government', 
         'control', 'value', 'few', 'generation', 'service', 'national',
         'tradition', 'government', 'mention', 'proposal']
""" a = set([i for i in words if len(words) > 6])         
print(len(a)) """
a = set(words)
c = 0
for i in a:
    if len(i) > 6:
        c += 1
print(c)

