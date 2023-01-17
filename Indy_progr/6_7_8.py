persons= [
    ('Bob Moore', 330000, 'M', '1635777202'),
    ('Gina Moore', 12500, 'F', '1639999999'),
         ]
data = {}
for i in persons:
    data.update({i[0]:{"salary":i[1],"gender":i[2],"passport":i[3]}})
print(data)