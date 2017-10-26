""" Demonstrating an object with regulated properties
"""
from class1 import obj1

# Object can be initialized like any others
thing1 = obj1("first property", "second property")
# Can set any properties like normal
thing1.prop3 = 42
print(thing1.prop1, thing1.prop2, thing1.prop3)

# Fails when attempting to set an unallowed property
thing1.someOtherProp = 67
