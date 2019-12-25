class Singleton():
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance
    
    # _instance = None
    # def __new__(cls, *args, **kwargs):
    #     if not cls._instance:
    #         cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
    #     return cls._instance

    def show(self):
        print(id(self))

instance1 = Singleton()
instance2 = Singleton()
instance1.show()
instance2.show()
print(isinstance(instance1, Singleton))
print(id(instance1) == id(instance2))
