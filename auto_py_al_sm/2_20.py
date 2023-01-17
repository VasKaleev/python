lines = ["one", "two", "three"]
with open('doc/demofile.txt', 'a',  encoding='utf-8') as f:
    for line in lines:
        f.write(line + '\n')