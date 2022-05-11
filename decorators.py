from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Tardo " + str(time_elapsed.total_seconds()) + " segundos en ejecutarse")
    return wrapper

@execution_time
def time():
    for _ in range(1, 1000000):
        pass

@execution_time
def sum(a: int, b:int) -> int:
    print(int(a + b))
    return a + b

@execution_time
def regards(name = "George") -> str:
    print("Saludos " + name)

time()
sum(16, 55)
regards("Ken")