import xml.etree.ElementTree as ET

try:
    tree=ET.parse("kraj.xml")
    root = tree.getroot()

    for child in root:
        print(f'tag: {child.tag}, atrybyuty: {child.attrib}')

    print("wybrane elementy: ")
    print(root[0])
    print(root[0][1])
    print(root[0][1].text)

except Exception as exc:
    print(exc)
