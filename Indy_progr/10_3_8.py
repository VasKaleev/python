names = [("Monica", "Waters"), ("Juan", "Lee"), ("Donna", "Walker")]
new_names = list(map(lambda x: (x[0] + " " + x[1]), names))
print(new_names)
