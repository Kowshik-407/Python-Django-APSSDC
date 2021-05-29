#Inheritance

# Single level Inheritance ::> one parent class and any one child

class classA:
    a , b = 10 , 20
    def display():
        return 'I am from Class A'

class classB(classA):
    c , d = 7 , 15
    def show():
        return 'I am from Class B'
    def mul():
        return classB.c * classB.d

# Multi level Inheritance ::> One or more parents and one or more childs

class classC:
    def C():
        return 'I am from classC'

class classD(classC):
    def D():
        return 'I am from classD'

class classE(classD):
    def E():
        return 'I am from classE'

# Multiple Inheritances ::> More than one parent and one child

class classF:
    def F():
        return 'I am from classF'

class classG:
    def G():
        return 'I am from classG'

class classH(classF, classG):
    def H():
        return 'I am from classH'


