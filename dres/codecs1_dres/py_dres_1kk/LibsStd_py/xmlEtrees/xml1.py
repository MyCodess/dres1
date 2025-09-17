# Py3/Doc/html/library/xml.etree.elementtree.html
# pydoc1 xml , pydoc1 xml.etree.ElementTree

"""
- Py3/Doc/html/library/xml.etree.elementtree.html  :
- 'ElementTree' represents the whole XML document as a tree, and 'Element' represents a single node in this tree
- xml-files read/write:  ElementTree
- xml-elemnts handle:    Element
- 
"""

import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()
for child in root:
    print(child.tag, child.attrib)
print("__root.tag:   ", root.tag)
print("__root-0-1:   ", root[0][1].text)

####################  from string:
print('------------------------------------------------------------')
xmlsstr1 = """ <applications> <application> <name>AppName</name> <comment>Comment</comment> <owner> <id>3</id> </owner> <editors> <editor> <id>4</id> </editor> </editors> <viewers> <viewer> <id>5</id> </viewer> </viewers> <customer> <id>24</id> </customer> </application> </applications> """
xmlsstr1 = """
<services>
    <service xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="singleServiceDTO">
        <name>icmp service</name>
        <comment>New service</comment>
        <type>icmp_service</type>
        <max>3</max>
        <min>3</min>
        <timeout>1</timeout>
    </service>
    <service xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="singleServiceDTO">
        <name>ip service</name>
        <comment>IPSEC Authentication Header Protocol</comment>
        <type>ip_service</type>
        <max>51</max>
        <min>51</min>
        <timeout>default</timeout>
    </service>
</services>
"""
root = ET.fromstring(xmlsstr1)
for child in root:
    print('tag:  ', child.tag, '  --  ', 'attrib:  ', child.attrib)
print("__root.tag:   ", root.tag)
print("__root-0-1-text:   ", root[0][1].text)
for child1 in root.iter('service'):
    print(child1.attrib)
