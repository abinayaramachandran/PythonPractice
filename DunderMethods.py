# # DunderMethods
# In Python, a class can have special methods that are invoked by special syntax (such as arithmetic operations or slicing) by defining methods with certain names.

# These methods are called dunder methods or magic methods, although they don’t have any magic in it. They are Python’s approach to operator overloading.

# They are used also to emulate some built-in types and can be used to enrich your classes in a more pythonic way.

# Initialization Dunder Methods
class A:
  def __new__(cls):
    print('Creation of A')
    instance = super().__new__(cls)
    return instance
  
  def __init__(self):
    print('Initialization')

  def __del__(self):
    print('Delete')

a = A()
del a

# Representation Dunder Methods
# Useful to get a string that represents the class instance.
class B:
    def __init__(self, a):
        self.a = a

    # repr is generally used to show formal represenation of that object
    def __repr__(self):
        return f'B ({self.a})'

    # str id generally used to show casual represenation of that object
    def __str__(self):
        return f'B with {self.a}'

    def __bytes__(self):
        return self.a.to_bytes(4, byteorder='big')

    def __format__(self, spec):
        if spec == 'f':
            return str(self.a)
        return str(self)

b = B(10)
print(repr(b))
print(str(b))
print(bytes(b))
print(format(b, 'f'))

# Comparison Dunder Methods
class C:
    def __init__(self, age):
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age

    def __hash__(self):
        return hash(self.age)

    def __bool__(self):
        return self.age > 0

alice = C(15)
bob = C(30)
rel = 'younger' if alice < bob else 'older'
print(f'Alice is {rel} than Bob')
print(hash(alice))


class D:
    '''A class that contains a value and implements an access counter.
    The counter increments each time the value is changed.'''
    def __init__(self, val):
        super().__setattr__('counter', 0)
        super().__setattr__('value', val)

    def __setattr__(self, name, value):
        if name == 'value':
            super().__setattr__('counter', self.counter + 1)
        super().__setattr__(name, value)

    def __delattr__(self, name):
        if name == 'value':
            super().__setattr__('counter', self.counter + 1)
        super().__delattr__(name)

d = D(10)
print(d.value, d.counter)
d.value = 11
print(d.value, d.counter)


class Celsius:
    '''Descriptor for celsius value.'''
    def __init__(self, value=0.0):
        self.value = float(value)
    
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)


class Fahrenheit:
    '''Descriptor for farenheit value.'''
    def __get__(self, instance, owner):
        return (instance.celsius * 9 / 5) + 32.0

    def __set__(self, instance, value):
        instance.celsius = (value - 32) * 5 / 9


class Temperature:
    celsius = Celsius()
    fahrenheit = Fahrenheit()

e = Temperature()
e.celsius = 10
print(f'{e.celsius} ºC = {e.fahrenheit} ºF')
e.fahrenheit = 45
print(f'{e.celsius} ºC = {e.fahrenheit} ºF')