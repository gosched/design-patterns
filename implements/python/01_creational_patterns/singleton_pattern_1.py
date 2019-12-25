class SingletonClass:

    __instance = None
    def __new__(cls):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

instance1 = SingletonClass()
instance2 = SingletonClass()

print(id(instance1), id(instance2), instance1 is instance2)