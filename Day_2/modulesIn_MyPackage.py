Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from MyPackage import MyModule
>>> from MyPackage import *]
SyntaxError: invalid syntax
>>> from MyPackage import *
>>> MyModule.ece()
'Welcome to ECE Students'
>>> MyModule.classA.A()
'I am from ClassA'
>>> Classes.ClassB.show()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    Classes.ClassB.show()
NameError: name 'Classes' is not defined
>>> Classes.classB.show()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    Classes.classB.show()
NameError: name 'Classes' is not defined
>>> Classes.classC.C()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    Classes.classC.C()
NameError: name 'Classes' is not defined
>>> from MyPackage.Classes import classB
>>> classB.show()
'I am from Class B'
>>> classB.mul()
105
>>> from MyPackage.Classes import classE
>>> classE.E
<function classE.E at 0x000001E759CD1A60>
>>> classE.E()
'I am from classE'
>>> classD.D()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    classD.D()
NameError: name 'classD' is not defined
>>> classE.D()
'I am from classD'
>>> classE.C()
'I am from classC'
>>> 
