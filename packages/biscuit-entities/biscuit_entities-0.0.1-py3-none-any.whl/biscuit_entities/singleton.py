# Singleton
# ------------------------------
# A singleton class. Ensures that at most one instance of this
# class exists at runtime. If an instance already exists, the 
# constructor returns that instance. If no such instance exists,
# the constructor creates one, calls its __setup__ method, and
# assigns that instance to the class. 
class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            cls.instance.__setup__()
        return cls.instance

    def __setup__(self):
        pass