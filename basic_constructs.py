"""
Python is 
* Dynamically typed: 
  * Frowned upon in large enterprise apps which use JVM or DotNet platforms with strong typing.   
* Interpreted: 
  * Implies slower than pure compiled language like C++ and Bytecode+JIT Compiled JVM Platform.  
* Less verbose 
  * No explicit brackets to indent (space is used for it). No type delaration 
  * Ability to express complex statements in single line using hight level data types
* Faster to develop and prototype
* There has best developer ecosystem (libraries and support) around data science, ML and AI. 
* It has support of Object Oriented programming and highly efficient data structure support and extensive standard library.
* It supports REPL
"""

# print and many other methods of standard python library are built in and don't even need to be imported. 
# also observe no semicolons needed ( can use them but not needed) 
# strings literals can be expressed using single or double qoutes. Choose one in project for consistency and which needs less escaping.  
print('hello world')

# no type declaration. It is interpreted. Only variable definition via initialization is needed
boolean_variable = True; 
# if doesnt need paranthesis (can work with parenthesis as well), just a colon in end
# recommended to use 4 spaces to express indent. Can use others but keep it consistent.
if boolean_variable: 
    print('Variable was true')


x = 24
if x > 20:
    print(f"value greater than 20: {x}") # parameterized expressions in string using f or formatted strings. Available since 3.6
elif x > 10 and x <=20: # elif and NOT else if
    print(f"value lies in (10,20], value: {x}")
else:
    print(f"values lies in (-infinity,10], value {x}")    


# ITERATION ( Iterables are any objects which have special methods __iter__ and __next__ . These can be explicitly called using iter(),next() )
greet = "Namaste"
for i in greet: # x in Iterable Type followed by : , type can be string, list, tuple which have __iter__ method 
    print(i)


# multi-assignments can be done with comma 
print("fibonacci")
a,b = 0,1
while a < 6:
    print(a, end = ",") # python supports both position argument and keywork argument. We can use both but keyword argument cannot come before position argument
    a, b = b, a+b # first a= b and then b = a+b

print('\n')

# Basic types
my_var_int = 1
my_var_float = 1.2

# SEQUENCE TYPES
# List is represented using square brackets. It is ordered, mutable and can contain heterogenous types.
my_list_1 = [1,2,3]
my_list_2 = [1,2.0, 5.4]
my_concatenated_list = my_list_1 + my_list_2
my_appened_list = my_concatenated_list.append(100)
# Tuple is represented using () )brackets. It is ordered, IMMUTABLE and can contain heterogenous types. 
my_tuple = (1,2,3)
# range: Represents an immutable sequence of numbers, often used for looping a specific number of times.

# MAPPING TYPES
# dictionary (dict) : UNordered, Mutable key value pair. 
# Key should always have immutable type like string, number or tuples. 
# Key cannot  be duplicated
# Represented using {} curly braces with comma separated "key":"value"  
# It is iterable but iter gives key value
my_map = {'foo': '95', 'bar': '95'}
print('value for key foo is ',my_map.get('foo'))
print('value for unavailable key is ',my_map.get('zoo'))
my_map['zoo'] = 99
print('value for newly added key zoo is ',my_map.get('zoo'))

my_map.keys() # A set like object (dict_keys) which gives a view of the keys. It it iterable. 
my_map.values() # an object (dict_values)which gives view of values. It is iterable.

for key in my_map:
    print(key)
for key in my_map.keys():
    print(key)
for value in my_map.values():
    print(value)
for key,value in my_map.items():
    print(key,value)   
for key,value in my_map.copy().items(): # iterate over shallow copy of map.
    print(key,value)     

# concat of among ints  & floats leads to mathematical addition. 
# concat using + can be done for same data type. string with string, list with list. For ex list cannot be concatenated with individual item.




print('"Yay", double qoutes do not need escape is string expressed using single qoutes')
print("single qoutes doesn't need escape if string expressed using double qoutes")
# escape using \ when needed and using r before string to convey that \ should not be escaped by telling interpreter that it is a raw string.
# multi line string using triple qoutes """
print("""
      Select *
      from myschema.my_table 
      where id = 123
      """)
# when you dont want new lines you can have srings next to each other in paranthesis.
# this cannot be done for variable and literal, only literals. You need plus for former.
print('Hello ' 
      'World in two strings next to each other are automatically concatenated')
my_str_for_index_ex = 'Hi There'
print(my_str_for_index_ex[0]) # stings can be indexed using [index].
print(my_str_for_index_ex[1:5]) # first index inclusive, second exclusive.
# Python strings are immutable (unlike java script)
# . i.e. doring  my_str_for_index_ex[0] = 'L' will fail with object assignment not supported
# using inbuilt fun len to get length of string
print("length of string " + my_str_for_index_ex + " is " , len(my_str_for_index_ex)); 

# Object oriented programming
# Class members vs object members , static vs class vs instance functions. Dunder instance functions as form of polymorphism.

# Concurrency and parallism
# https://medium.com/pythons-gurus/understanding-concurrency-and-parallelism-in-python-a-comparative-guide-with-java-and-c-6167f3732b15




