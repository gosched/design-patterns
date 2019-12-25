import datetime

def my_decorator(func):
    def wrap(*args, **kwargs):
        return 'my_decorator ' + func(*args, **kwargs)
    return wrap

@my_decorator
def hello1(name):
    return 'hello ' + name

print(hello1('abc'))
print('hello1.__name__ :', hello1.__name__)
print()

def tag_decorator(tag_name):
    def decorator(func):
        def wrap(*args, **kwargs):
            print(datetime.datetime.now())
            return func(*args, **kwargs)
        return wrap
    return decorator

@tag_decorator('tag_tag_tag_!!!')
def hello2(name):
    return 'hello ' + name

print(hello2('abc'))
print('hello2.__name__ :', hello2.__name__)
print()

from functools import wraps
def tag(tagname):
    def decorator(func):
        @wraps(func)
        def hi(name):
            return '<{0}>{1}</{0}>'.format(tagname, func(name))
        return hi
    return decorator

@tag('my_tag')
def hello3(name):
    return 'hello ' + name

print(hello3('abc'))
print('hello3.__name__ :', hello3.__name__)
print()
