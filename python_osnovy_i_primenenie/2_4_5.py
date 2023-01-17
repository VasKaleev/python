import os

with open('result.txt', 'a') as f:
    for current_dir, dirs, files in os.walk('main'):
        if list(filter(lambda x: x.endswith('.py'), files)):
            f.write('{}\n'.format(current_dir))
