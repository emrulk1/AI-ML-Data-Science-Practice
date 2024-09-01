import sys
import xml.etree.ElementTree as etree

total_attribues = 0
def get_attr_number(node):
    # your code goes here
    global total_attribues
    total_attribues += len(node.attrib)
    for child_node in node :
        total_attribues + get_attr_number(child_node)
    return total_attribues




if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))