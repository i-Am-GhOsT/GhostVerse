import time

class Decorators:
    def time_it(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args,**kwargs)
            end = time.time()
            print(func.__name__+" Took "+ str((end-start)*1000)+"ms.")
            return result
        return wrapper