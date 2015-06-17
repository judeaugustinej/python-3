"""Simple usage for slice"""

>>> land_line = "080-2286567"
>>> STATE_CODE = slice(0,3)
>>> land_line[STATE_CODE]
'080'
>>> LAND_NUM = slice(4,11)
>>> land_line[LAND_NUM]
'2286567'
>>> 
>>>
