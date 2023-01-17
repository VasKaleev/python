import xml.etree.ElementTree as ET
xm = input()
root = ET.fromstring(xm)
colors = {"red": 0, "green": 0, "blue": 0}
def getcubes(root, value):
    colors[root.attrib['color']] += value
    for child in root:
        getcubes(child, value+1)
getcubes(root, 1)
print(colors["red"], colors["green"], colors["blue"])   

