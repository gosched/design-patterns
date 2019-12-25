def singleton(cls):
    _instance = {}

    def create():
        if cls not in _instance:
            _instance[cls] = object.__new__(cls)
        return _instance[cls]
    return create

@singleton
class TestClass():
    pass

instance1 = TestClass()
instance2 = TestClass()
print(id(instance1), id(instance2))
print(id(instance1) == id(instance2))
