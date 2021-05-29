print('Hello Django')

# Functions 

def hello():
    return "Hello Everyone!! This is Kowshik407"


def add():
    a , b = 10, 20
    return a + b


def add_dynamic(a,b):
    return a + b


# Classes


class hello1:
    a , b = 10 , 20
    def hi():
        return 'Hello!! Welcome to Django'

class math:
    def add(n1, n2):
        return n1 + n2
    def sub(n1, n2):
        return n1 - n2
    
class workshop:
    def lang():
        r = ['python', 'javascript','java']
        return r
    def web():
        r = ['django','flask','reactJs','nodeJs','OOPS','servlets']
        return r

# Objects

class cal:
    a , b = 10 , 20
    def div():
        return cal.a / cal.b
    def power():
        return cal.a ** cal.b

# Constructors

class student:
    def __init__(self, name, rollno):
        self.name       =    name
        self.rollno     =    rollno

    def display(self):
        return { 'name' : self.name , 'rollno' : self.rollno }


class student1:
    def __init__(self):
        return 'Hello Django'
    def display(name, rollno):
        return { 'name' : name , 'rollno' : rollno }


