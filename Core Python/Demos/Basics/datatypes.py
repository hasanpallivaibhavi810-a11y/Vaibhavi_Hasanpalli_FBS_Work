#numeric
#1.int
x=10

#2.float
a=3.14
print(type(a))

#3.complex  
x=5+10j #real + imaginary
print(type(x))


##Text

#1.str
x='Firstbit'  #single line string
x="Firstbit"  #single line string

x='''This is first line.  
This is second line'''  #Multi line string

x="""This is first line.  
This is second line.""" #Multi line string
print(x)
print(type(x))


###sequential

#1.list
x=[10,20,30,40]
print(x)
print(type(x))

#2.tuple
x=(10,20,30,40)

#3.range
x=range(1,10)
print(x)
print(type(x))


###set 

#1.set
x={10,20,30,40}
print(type(x))

#2.frozenset
x=frozenset({10,20,30,40})
print(x)
print(type(x))


###Mapping
#1. dict
x={1:'Python',2:'Java',3:'C'}
print(x)
print(type(x))


###Other
#1. Boolean
x=False
x=True
print(x)
print(type(x))

#2. Nonetype
x=None
print(x)
print(type(x))

