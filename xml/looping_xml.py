import xml.etree.ElementTree as ET

input = '''
<stuff>
<users>
<user x="2">
<id>001</id>
<name>Chuck</name>
</user>
<user x="7">
<id>009</id>
<name>Brent</name>
</user>
</users>
</stuff>'''

tree = ET.fromstring(input)
lst  = tree.findall('users/user')
print('User count: ',len(lst))

for item in lst:
    print('Name: ',item.find('name').text)
    print('ID: ',item.find('id').text)
    print('Attribute: ',item.get('x'))
"""
devstack@openstack:~/Documents/web_python/xml_my$ python looping_xml.py 
('User count: ', 2)
('Name: ', 'Chuck')
('ID: ', '001')
('Attribute: ', '2')
('Name: ', 'Brent')
('ID: ', '009')
('Attribute: ', '7')
devstack@openstack:~/Documents/web_python/xml_my$ python3 looping_xml.py 
User count:  2
Name:  Chuck
ID:  001
Attribute:  2
Name:  Brent
ID:  009
Attribute:  7
devstack@openstack:~/Documents/web_python/xml_my$ 
"""
