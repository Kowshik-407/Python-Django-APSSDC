Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
====== RESTART: C:/Users/Srinivas/Desktop/Python_Django/Day_2/Sample.py ======
>>> classA.a
10
>>> classB.b
20
>>> classA.display()
'I am from Class A'
>>> classB.c
7
>>> classB.d
15
>>> classB.a
10
>>> classB.b
20
>>> classB.show
<function classB.show at 0x000001C23F504048>
>>> classB.show()
'I am from Class B'
>>> classB.mul()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    classB.mul()
  File "C:/Users/Srinivas/Desktop/Python_Django/Day_2/Sample.py", line 11, in mul
    return c * d
NameError: name 'c' is not defined
>>> classB.mul()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    classB.mul()
  File "C:/Users/Srinivas/Desktop/Python_Django/Day_2/Sample.py", line 11, in mul
    return c * d
NameError: name 'c' is not defined
>>> obj = classA
>>> obj.a
10
>>> obj.b
20
>>> obj.display'
SyntaxError: EOL while scanning string literal
>>> obj.display()
'I am from Class A'
>>> ob = classB
>>> ob.c
7
>>> ob.d
15
>>> ob.a
10
>>> ob.b
20
>>> ob.show()
'I am from Class B'
>>> ob.mul()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    ob.mul()
  File "C:/Users/Srinivas/Desktop/Python_Django/Day_2/Sample.py", line 11, in mul
    return c * d
NameError: name 'c' is not defined
>>> 
====== RESTART: C:/Users/Srinivas/Desktop/Python_Django/Day_2/Sample.py ======
>>> ob = classB
>>> ob.mul()
105
>>> 
====== RESTART: C:/Users/Srinivas/Desktop/Python_Django/Day_2/Sample.py ======
>>> classC.c()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    classC.c()
AttributeError: type object 'classC' has no attribute 'c'
\
>>> classC.C()
'I am from classC'
>>> classD.D()
'I am from classD'
>>> classE.E()
'I am from classE'
>>> obj = classC.C()
>>> obj = classC
>>> obj.C()
'I am from classC'
>>> ob = classD
>>> ob.D()
'I am from classD'
>>> o = classE
>>> o.E()
'I am from classE'
>>> o.C()
'I am from classC'
>>> o.D()
'I am from classD'
>>> ob.E()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    ob.E()
AttributeError: type object 'classD' has no attribute 'E'
>>> ob.C()
'I am from classC'
\
>>> 
====== RESTART: C:/Users/Srinivas/Desktop/Python_Django/Day_2/Sample.py ======
Traceback (most recent call last):
  File "C:/Users/Srinivas/Desktop/Python_Django/Day_2/Sample.py", line 41, in <module>
    class classH(classF, classG):
NameError: name 'classG' is not defined
>>> obj = classF
>>> obj.F()
'I am from classF'
>>> ob = classG
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    ob = classG
NameError: name 'classG' is not defined
>>> ob = classG
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    ob = classG
NameError: name 'classG' is not defined
>>> 
====== RESTART: C:/Users/Srinivas/Desktop/Python_Django/Day_2/Sample.py ======
>>> ob = classG
>>> ob.G()
'I am from classG'
>>> o = classH
>>> o.H()
'I am from classH'
>>> o.G()
'I am from classG'
>>> o.F()
'I am from classF'
>>> 
