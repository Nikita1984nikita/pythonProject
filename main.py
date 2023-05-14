import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} execution time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper
@measure_time
def test_func1():
    time.sleep(1)

@measure_time
def test_func2():
    for i in range(10000000):
        pass

test_func1()
test_func2()

