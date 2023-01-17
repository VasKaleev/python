sp = input().split()
a = [int(i) for i in sp]
tree_dict = {a[-2]: a[-1]}

for key in reversed(a[:-2]):
    tree_dict = {key: tree_dict}
print(tree_dict)
