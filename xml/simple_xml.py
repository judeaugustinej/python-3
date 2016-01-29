import xml.etree.ElementTree as ET

data = '''
<person>
<name>Chuck</name>
<phone type="intl">
+1 734 303 4456
</phone>
<email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print(type(tree))

print('Name: ',tree.find('name'))
print('Name: ',tree.find('name').text)

print('Attr for email hide', tree.find('email').get('hide'))

print('ph no: ',tree.find('phone').text)
print('ph attr tye value ',tree.find('phone').get('type'))

"""
devstack@openstack:~/Documents/web_python/xml_my$ python simple_xml.py 
<class 'xml.etree.ElementTree.Element'>
('Name: ', <Element 'name' at 0x7fd92947fdd0>)
('Name: ', 'Chuck')
('Attr for email hide', 'yes')
('ph no: ', '\n+1 734 303 4456\n')
('ph attr tye value ', 'intl')
devstack@openstack:~/Documents/web_python/xml_my$ python3 simple_xml.py 
<class 'xml.etree.ElementTree.Element'>
Name:  <Element 'name' at 0x7fbb539d0408>
Name:  Chuck
Attr for email hide yes
ph no:  
+1 734 303 4456

ph attr tye value  intl
devstack@openstack:~/Documents/web_python/xml_my$ 

"""
