import string

fp = open('romeo_new.txt')
for line in fp:
    print(line)
    line = line.translate(None, string.punctuation)
    print(line)
"""
But,! soft what light through yonder window breaks,

But soft what light through yonder window breaks

It is@ the east and Juliet is the sun,

It is the east and Juliet is the sun

Arise fair sun and kill the envious moon,

Arise fair sun and kill the envious moon

Who is already sick and pale with grief.

Who is already sick and pale with grief


"""
