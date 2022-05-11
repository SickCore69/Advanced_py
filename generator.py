import time
def Fibo_gen():
    n1 = 0
    n2 = 1
    count = 0
    while True:
        if count == 0:
            count += 1
            yield n1
        elif count == 1:
            count += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux 
            yield aux
if __name__ == '__main__':
    fibonacci = Fibo_gen()
    for element in fibonacci:
        print(element)
        time.sleep(0.5)