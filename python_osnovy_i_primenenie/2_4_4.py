with open("dataset_24465_4.txt", "r") as f, open("2_4_4n.txt", "w") as f1:
    x = f.read()
    x = x.splitlines()
    x1 = x[::-1]
    for i in x1:
        f1.write(i + "\n")
