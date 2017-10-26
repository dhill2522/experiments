# This is a class where only prop1, prop2, and prop3 can be set
# Any other properties raise an AttributeError
class obj1(object):
    def __init__(self, arg1, arg2):
        # Note that even these setters will be redirected through __setattr__
        self.prop1 = arg1
        self.prop2 = arg2
    # This is automatically called before any property is set. Effectively
    # captures property setting for the entire class.
    def __setattr__(self, arg, value):
        """
        arg:        name of the property that is attempting to be set
        value:      value for that attempted property
        """
        if arg in ("prop1", "prop2", "prop3"):
            # Note that calling self.prop1 = value would cause infinite recursion
            # To get around this we need to insert the value directly into self.__dict__
            self.__dict__[arg] = value
        else:
            # Note that the failure can be handled however we want, including 'pass'
            print(str(arg) + " is not a valid property of obj1!")
            raise AttributeError
