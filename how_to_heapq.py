"""Basic usuage of heapq module"""

#The most important feature of a heap is that heap[0] is always the smallest item

>>> import heapq
>>>
>>> temperature = [1,2,3,4,-4,0,-12,33,7]
>>>
>>> temperature
[1, 2, 3, 4, -4, 0, -12, 33, 7]
>>> heapq.heappush(temperature,-14)
>>>
>>> temperature
[-14, 1, 3, 4, 2, 0, -12, 33, 7, -4]
>>>
>>> type(temperature)
<class 'list'>
>>> heapq.heapify(temperature)
>>>
>>> type(temperature)
<class 'list'>

