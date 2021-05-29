Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import time
>>> time.ctime
<built-in function ctime>
>>> time.ctime()
'Tue Aug  4 14:45:49 2020'
>>> import os
>>> os.path()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    os.path()
TypeError: 'module' object is not callable
>>> os.cpath()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    os.cpath()
AttributeError: module 'os' has no attribute 'cpath'
>>> os.pwd()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    os.pwd()
AttributeError: module 'os' has no attribute 'pwd'
>>> os.getcwd()
'C:\\Users\\Srinivas\\AppData\\Local\\Programs\\Python\\Python36'
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> 
