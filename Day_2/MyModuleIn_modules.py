Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import MyModule
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import MyModule
ModuleNotFoundError: No module named 'MyModule'
>>> After inserting our MyModule in the path\
    
SyntaxError: invalid syntax
>>> import MyModule
>>> number()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    number()
NameError: name 'number' is not defined
>>> MyModule.number()
1
2
3
4
5
6
7
8
9
>>> EvenorOdd(7)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    EvenorOdd(7)
NameError: name 'EvenorOdd' is not defined
>>> MyModule.EvenorOdd(7)
'It is Odd'
>>> MyModule.ece()
'Welcome to ECE Students'
>>> MyModule.classA.A()
'I am from ClassA'
>>> 
