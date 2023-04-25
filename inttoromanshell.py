Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s="100"
s[-len(s)]
'1'
k=1
for i,j in enumerate(s):
    k=k*10

    
k
1000
for i,j in enumerate(len(s)-1):
    k=k*10

    
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    for i,j in enumerate(len(s)-1):
TypeError: 'int' object is not iterable
coouter=0
k=1
while counter<len(s)-1:
    k=k*10
    counter+=1

    
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    while counter<len(s)-1:
NameError: name 'counter'
