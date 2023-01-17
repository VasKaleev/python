from xml.etree import ElementTree
#xm = input()
tree = ElementTree.parse("1.xml")
root = tree.getroot()
print(root)
