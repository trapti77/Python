
#Problem1 --- Timing function execution

import time

def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper


@timer  # yaha pe timer laga diya ab iske mtlb ki example_fun function @timer function se hokar hi gujrega
def example_func(n):
    time.sleep(n)
    
# example_func(2)


#problem2 -- debugging function call

#basic decorator
# def debug(func):
#     def wrapper():
#         return func()
#     return wrapper
def hello():
    print("Hello this")

def debug(func):
    def wrapper(*args,**kwargs):
        args_value=', '.join(str(arg) for arg in args)
        kwargs_value=', '.join(f"{k}={v}" for k , v in kwargs.items())
        print(f"calling : {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args,**kwargs)

    return wrapper
    
    
@debug
def green(name,greeting="Hello"):
    print(f"{greeting}, {name}")
    

# green("Trapti")  
# output  -- calling : green with args Trapti and kwargs 
# Hello, Trapti

#problem 3 -- cache return value

def cache(func):
    cache_value={}
    print(cache_value)
    def wrapper(*args):
        if(args in cache_value):
            return cache_value[args]
        result= func(*args)
        cache_value[args]=result
        return result
    return wrapper

@cache
def long_running_func(a,b):
    time.sleep(4)
    return a+b

print(long_running_func(2,3))
print(long_running_func(2,3))
print(long_running_func(4,3))





    
