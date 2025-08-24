"""
Note on type hints in method params and class/object data members: 
While not strictly enforced by the Python interpreter, using type hints is a recommended convention 
that promotes code clarity, maintainability, and quality, especially in collaborative development environments.

Note on immutability: There is no explicit java like final construct. One can achieve immutability via 
* Option 1: Double underscored attributes with no setters, just constuctor or factory methods. 
* Option 2: For basic data container classes ( like java POJO), one can use @dataclass decorator with Frozen=true parameter.
  * from dataclasses import dataclass

Python supports multiple inheritance. 
Python doesn't have notion of abstract classes, methods.
Python doesn't have notion of interfaces.


"""


class Employee:
    # Public Class members: Capital by convention, 
    CITY_TO_CODE_PREFIX_MAP: dict = {"Hyderabad" :"HYD", "NewYork": "NYC"}

    # mentioned type in constuctor params explicitly
    def  __init__(self,name: str, code: str): 
        self.__name = name   ## Hidden object data member due to double underscore convention
        self.code = code     ## publicly accessible data member

    # instance methods have access to self (like java this) 
    def get_code_and_name_concatenated(self):
        return self.code + '' + self.__name 
    
    """
    They are class level methods ( equivalent to Java static methods). 
    These methods have access to cls as param which can be used to access class data members. 
    Like in java, they are accessed via Class name but in python they can also be accessed via object 
    Typical uses
    * Factory methods 
    * Class level opereations which need class level state and utilites
    """
    @classmethod  # called annotations in java and decorators in python.
    def get_code_prefix_by_city(cls, city: str) -> str : 
        return Employee.CITY_TO_CODE_PREFIX_MAP[city]
    """
    Differs from classmethods in the sense that they dont have access to self or cls and hence cant access class members or object members
    """
    @staticmethod
    def sample_static_method():
        print("static method called")

        

# No type declaration, no new keyword
e=  Employee("Harry Potter", "A123");
print(e.code);
# print(e.__name);  ## call will fail that there is no such attribute
print(e.get_code_and_name_concatenated())
print(Employee.CITY_TO_CODE_PREFIX_MAP);
print(e.get_code_prefix_by_city("Hyderabad"))
e.sample_static_method()


class Car:
    def __init__(self, company: str):
        self.company = company
        print("Car initialized")
    
    def who_am_i():
        print("I am Car")

class BMW(Car):
    def __init__(self, company,  is_automatic=True):
        super().__init__(company)
        self.is_automatic = is_automatic

    def who_am_i(self):
        print("I am BMW")


car = BMW("BMW",False)
car.who_am_i();            


