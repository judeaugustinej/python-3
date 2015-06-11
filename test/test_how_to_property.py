import unittest

import how_to_property

class PersonTestCase(unittest.TestCase):
  
  def setUp(self):
    self.personObj = how_to_property.Person("Jude",25)
    
  def test_delete_age(self):
    self.assertRaises(AttributeError,del self.personObj.name)
    
