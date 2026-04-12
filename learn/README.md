>>> mylistone=[1,2]
>>> mylisttwo=mylistone
>>> mylisttwo
[1, 2]
>>> mylistone='chai'
>>> mylistone[0]
'c'
>>> h1=[1,2,3]
>>> h2=h1
>>> h1
[1, 2, 3]
>>> h2
[1, 2, 3]
>>> h1[0]=55
>>> h1
[55, 2, 3]
>>> h2
[55, 2, 3]
>>> h2=h1[:]
>>> h1
[55, 2, 3]
>>> h2
[55, 2, 3]
>>> h1[1]=11
>>> h1
[55, 11, 3]
>>> h2
[55, 2, 3]
>>> m=[1,2,3]
>>> n=m 
>>> m==n  # here == check value 
True
>>> m is n
True
>>> m=[1,2,3]
>>> m==n
True
>>> m is n  # here 'is' check reference 
False
>>>

#NUMBER IN PYTHON

>>> result
0.3333333333333333
>>> repr('chai')
"'chai'"
>>> str('chai')
'chai'
>>> print('chai')
chai
>>> 1<2
True
>>> 2<1
False
>>> 5.0==4.0
False
>>> x,y,z
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
>>> x=1
>>> y=2
>>> z=3
>>> x,y,z
(1, 2, 3)
>>> x<y<z
True
>>> x<y and y<z
True
>>> x<y or y>z
True
>>> import math
>>> math.floor(3.5)
3
>>> math.ceil(3.5)
4
>>> math.trunc(2.8)
2
>>> math.trunc(-2.8)
-2
>>> math.floor(-3.5)
-4
>>> 2+1j
(2+1j)
>>> (2+1j)*3
(6+3j)
>>> int(64)
64
>>> int('64',8)
52
>>> int('64',2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 2: '64'
>>> int('1000',2)
8
>>> int('64',16) 
100
>>> x=1
>>> x<<2
4
>>> import random
>>> random.random()
0.3282411653710833
>>> random.random()
0.4171116590785062
>>> random.random()*100
81.01867743864398
>>> random.randint(1,100)
99
>>> random.randint(1,100)
4
>>> random.randint(1,100)
22
>>> random.choice(["lemon","masala","ginger"])
'masala'
>>> random.choice(["lemon","masala","ginger"])
'masala'
>>> random.choice(["lemon","masala","ginger"])
'ginger'
>>> from decimal import Decimal
>>> Decimal('0.1')+Decimal('0.1')+Decimal('0.1')
Decimal('0.3')
>>> 0.1+0.1+0.1
0.30000000000000004
>>> (0.1+0.1+0.1)-0.3
5.551115123125783e-17
>>> Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3')
Decimal('0.0')
>>>     
>>> 
>>> setone={1,2,3,4}
>>> setone & {1,3}
{1, 3}
>>> setone | {1,3}
{1, 2, 3, 4}
>>> setone | {1,3,7}
{1, 2, 3, 4, 7}
>>> setone - {1,3,7}
{2, 4}
>>> setone
{1, 2, 3, 4}
>>> setone - {1,2,3,4}
set()
>>> type({})
<class 'dict'>
>>> type(True)
<class 'bool'>
>>> True==1
True
>>> 0
0
>>> False
False
>>> False==0
True
>>> 


# STRING 

>>> chai='Masala Chai'
>>> chai
'Masala Chai'
>>> for letter in chai:
... 
  File "<stdin>", line 2
    
    ^
IndentationError: expected an indented block after 'n line 1
>>> for letter in chai:
...     print(letter)
... 
M
a
s
a
l
a
 
C
h
a
i
>>> chai="He said, "masala chai is awesome" "
  File "<stdin>", line 1
    chai="He said, "masala chai is awesome" "
                    ^^^^^^
SyntaxError: invalid syntax
>>> chai="He said,\ "masala chai is awesome \" "
  File "<stdin>", line 1
    chai="He said,\ "masala chai is awesome \" "
                     ^^^^^^
SyntaxError: invalid syntax
>>> chai="He said,\ " Masala chai is awesome \" "
  File "<stdin>", line 1
    chai="He said,\ " Masala chai is awesome \" "
                      ^^^^^^
SyntaxError: invalid syntax
>>> 


# LIST
>>> list= list()
>>> tea_variety=["masala","white","black","green"]
>>> tea_variety
['masala', 'white', 'black', 'green']
>>> print(tea_variety[-1])
green
>>> print(tea_variety[1:3])
['white', 'black']
>>> print(tea_variety[:3]) 
['masala', 'white', 'black']
>>> print(tea_variety[2:]) 
['black', 'green']
>>> tea_variety[3]="herbal"
>>> tea_variety            
['masala', 'white', 'black', 'herbal']
>>> tea_variety[1:2]="Lemon"
>>> tea_variety             
['masala', 'L', 'e', 'm', 'o', 'n', 'black', 'herbal']
>>> tea_variety=["masala","white","black","green"]
>>> tea_variety
['masala', 'white', 'black', 'green']
>>> tea_variety[1:3]=["ginger","Oolong"]
>>> tea_variety
['masala', 'ginger', 'Oolong', 'green']
>>> tea_variety[1:1]=["test","test"]
>>> tea_variety
['masala', 'test', 'test', 'ginger', 'Oolong', 'green']
>>> tea_variety[1:3]=[]                 
>>> tea_variety        
['masala', 'ginger', 'Oolong', 'green']
>>> for tea in tea_variety:
...     print(tea)
... 
masala
ginger
Oolong
green
>>> if "Oolong" in tea_variety:
...     print("I have oolong tea")
... 
I have oolong tea
>>> tea_variety.append("black")
>>> tea_variety                
['masala', 'ginger', 'Oolong', 'green', 'black']
>>> tea_variety.pop()
'black'
>>> tea_variety      
['masala', 'ginger', 'Oolong', 'green']
>>> tea_variety.remove("Oolong")
>>> tea_variety                 
['masala', 'ginger', 'green']
>>> tea_variety.insert(1,"Oolong")
>>> tea_variety
['masala', 'Oolong', 'ginger', 'green']
>>> tea_variety_copy=tea_variety.copy()
>>> tea_variety_copy                   
['masala', 'Oolong', 'ginger', 'green']
>>> tea_variety_copy.append("lemon")
>>> tea_variety_copy                
['masala', 'Oolong', 'ginger', 'green', 'lemon']
>>> tea_variety
['masala', 'Oolong', 'ginger', 'green']
>>> squared_nums=[x**2 for x in range(10)]
>>> squared_nums                          
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> range(10)
range(0, 10)
>>> 


# Dictionary

>>> chai_types={"Masala":"spicy","Ginger":"Zesty","Green":"Mild"}
>>> chai_types
{'Masala': 'spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
>>> chai_types["Ginger"]
'Zesty'
>>> chai_types.get("Ginger")
'Zesty'
>>> for chai in chai_types:
...     print(chai)
... 
Masala
Ginger
Green
>>> for chai in chai_types:
...     print(chai, chai_types[chai])
... 
Masala spicy
Ginger Zesty
Green Mild
>>> for key,value in chai_types.items():
...     print(key, value)
... 
Masala spicy
Ginger Zesty
Green Mild
>>> if "Masala" in chai_types:
...     print("I have Masala chai")
... 
I have Masala chai
>>> chai_types["Earl Grey"]="Citrus"
>>> chai_types
{'Masala': 'spicy', 'Ginger': 'Zesty', 'Green': 'Mild', 'Earl Grey': 'Citrus'}
>>> chai_types.pop("Earl Grey")
'Citrus'
>>> chai_types
{'Masala': 'spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
>>> chai_types.popitem()
('Green', 'Mild')
>>> chai_types          
{'Masala': 'spicy', 'Ginger': 'Zesty'}
>>> del chai_types["Green"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Green'
>>> del chai_types["Masala"]
>>> chai_types              
{'Ginger': 'Zesty'}
>>> chai_types_copy=chai_types.copy()
>>> chai_types_copy                  
{'Ginger': 'Zesty'}
>>> tea_stop={
... "chai":{"Masala":"spicy","Ginger":"Zesty"},
... "Tea":{"Green":"Mild","Black":"Strong"}
... }
>>> tea_stop
{'chai': {'Masala': 'spicy', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}
>>> tea_stop.chai
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'chai'
>>> tea_stop["chai"]
{'Masala': 'spicy', 'Ginger': 'Zesty'}
>>> tea_stop["chai"]["Ginger"]
'Zesty'
>>> squared_num={x:x**2 for x in range(6)}
>>> squared_num                           
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
>>> squared_num.clea()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'clea'. Did you mean: 'clear'?
>>> squared_num.clear()
>>> squared_num        
{}
>>> keys=["Masala","Ginger","Lemon"]
>>> keys                            
['Masala', 'Ginger', 'Lemon']
>>> default_val="Delicious"
>>> new_dict=dict.fromkeys(keys,default_val)
>>> new_dict                                
{'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}
>>> 


# Tuples

# list can be changable but tuples cannt be change

# Iteration Tools Or Iteration lists
>>> f=open('chai.py')
>>> f.readline()
'import time\n'
>>> f.readline()
'print("chai is here")\n'
>>> f.readline()
'username="hitesh"\n'
>>> f.readline()
'print(username)'
>>> f.readline()
''
>>> f.readline()
''
>>> f=open('chai.py')
>>> f.__next__()
'import time\n'
>>> f.__next__()
'print("chai is here")\n'
>>> f.__next__()
'username="hitesh"\n'
>>> f.__next__()
'print(username)'
>>> f.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> for line in open('chai.py')
  File "<stdin>", line 1
    for line in open('chai.py')
                               ^
SyntaxError: expected ':'
>>> for line in open('chai.py'):
...     print(line)
... 
import time

print("chai is here")

username="hitesh"

print(username)
>>> for line in open('chai.py'):
...     print(line,end='')      
... 
import time
print("chai is here")
username="hitesh"
print(username)>>> 
>>> f=open('chai.py')           
>>> while True:
...     line=f.readline()
...     if not line: break
...     print(line,end='')
... 
import time
print("chai is here")
username="hitesh"
print(username)>>> 
>>> test="trapti"
>>> if not test:
...     print("chai")
...     
... 
>>> test="":         
  File "<stdin>", line 1
    test="":
           ^
SyntaxError: invalid syntax
>>> test="" 
>>> if not test:     
...     print("chai")     
... 
chai
>>> 
>>> myList=[1,2,3,4]
>>> I=iter(myList)
>>> I
<list_iterator object at 0x0000014E91D5B040>
>>> I.__next__()
1
>>> I.__next__()
2
>>> I           
<list_iterator object at 0x0000014E91D5B040>
>>> I.__next__()  
3
>>> I.__next__()
4
>>> I.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> 
>>> f=open('chai.py')
>>> iter(f) is f
True
>>> iter(f) is f.__iter__()
True
>>> myNewList=[1,2,3,4]
>>> I=iter(myNewList) is myNewList
>>> iter(myNewList) is myNewList  
False
>>> D={'a':1,'b':2}               
>>> for key in D.keys():
...     print(key)
... 
a
b
>>> I=iter(D)
>>> I
<dict_keyiterator object at 0x0000014E922A66B0>
>>> I.__next__()   
'a'
>>> I.__next__()
'b'
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> I=iter(D)   
>>> next(I)     
'a'
>>> next(I)
'b'
>>> range(3)
range(0, 3)
>>> R=range(3)
>>> I=iter(R)
>>> next(I)
0
>>> next(I)
1
>>> next(I)
2
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> 

