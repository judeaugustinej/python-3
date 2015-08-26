###What is context manager

```
A context manager is responsible for a resource within a code block,
possibly creating it when the block is entered and then cleaning it up after the block is exited.
For example, files support the context manager API to make it easy to ensure they are closed after 
all reading or writing is done.
```
####Example
```
with open('/home/jude/notes.txt', 'w') as f:
    f.write('I am going home')
# file is automatically closed
```
