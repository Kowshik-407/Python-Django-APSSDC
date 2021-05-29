Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========= RESTART: C:\Users\Srinivas\Desktop\Python_Django\Sample.py =========
Hello Django
>>> hello()
'Hello Everyone!! This is Kowshik407'
>>> add()
30
>>> add_dynamic(7,15)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    add_dynamic(7,15)
NameError: name 'add_dynamic' is not defined
>>> 
========= RESTART: C:\Users\Srinivas\Desktop\Python_Django\Sample.py =========
Hello Django
>>> add_dynamic(7,15)
22
>>> add_dynamic('Hello','Django')
'HelloDjango'
>>> 
========= RESTART: C:\Users\Srinivas\Desktop\Python_Django\Sample.py =========
Hello Django
>>> hello
<class '__main__.hello'>
>>> hello()
<__main__.hello object at 0x000002356BFF2DA0>
>>> 
========= RESTART: C:\Users\Srinivas\Desktop\Python_Django\Sample.py =========
Hello Django
>>> 
========= RESTART: C:\Users\Srinivas\Desktop\Python_Django\Sample.py =========
Hello Django
>>> hello
<function hello at 0x000001CD75AA1EA0>
>>> hello()
'Hello Everyone!! This is Kowshik407'
>>> hello.a
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    hello.a
AttributeError: 'function' object has no attribute 'a'
>>> hello1.a
10
>>> hello1.b
20
>>> hello1.hi()
'Hello!! Welcome to Django'
>>> 
========= RESTART: C:\Users\Srinivas\Desktop\Python_Django\Sample.py =========
Hello Django
>>> math
<class '__main__.math'>
>>> math.add()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    math.add()
TypeError: add() missing 2 required positional arguments: 'n1' and 'n2'
>>> math.add(7, 111)
118
>>> math.sub(7,7)
0
/
>>> '
SyntaxError: EOL while scanning string literal
>>> '
SyntaxError: EOL while scanning string literal
>>> '
SyntaxError: EOL while scanning string literal
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> clear
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
\
>>> clc
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    clc
NameError: name 'clc' is not defined
>>> clear all
SyntaxError: invalid syntax
>>> 
========= RESTART: C:\Users\Srinivas\Desktop\Python_Django\Sample.py =========
Hello Django
>>> workshop.lang()
['python', 'javascript', 'java']
>>> workshop.web()
['django', 'flask', 'reactJs', 'nodeJs', 'OOPS', 'servlets']
>>> 
========= RESTART: C:\Users\Srinivas\Desktop\Python_Django\Sample.py =========
Hello Django
>>> obj = cal
>>> obj.a
10
>>> obj.b
20
>>> obj.div()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    obj.div()
  File "C:\Users\Srinivas\Desktop\Python_Django\Sample.py", line 43, in div
    return a / b
NameError: name 'a' is not defined
>>> 
========= RESTART: C:\Users\Srinivas\Desktop\Python_Django\Sample.py =========
Hello Django
>>> obj = cal
>>> obj.div()
0.5
>>> obj.power()
100000000000000000000
>>> 
========= RESTART: C:\Users\Srinivas\Desktop\Python_Django\Sample.py =========
Hello Django
>>> obj = student('Kowshik', 407)
>>> obj.display()
{'name': 'Kowshik', 'rollno': 407}
>>> obj.name
'Kowshik'
>>> obj.rollno
407
>>> 
========= RESTART: C:\Users\Srinivas\Desktop\Python_Django\Sample.py =========
Hello Django
>>> obj = student'
SyntaxError: EOL while scanning string literal
>>> obj = student1
>>> obj.display()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    obj.display()
TypeError: display() missing 3 required positional arguments: 'self', 'name', and 'rollno'
>>> 
========= RESTART: C:\Users\Srinivas\Desktop\Python_Django\Sample.py =========
Hello Django
>>> obj = student1
>>> obj.display('kowshik', 407)
{'name': 'kowshik', 'rollno': 407}
>>> 
