from __future__ import division

def make_division(x: int)  -> int:
    def division(n: int)-> int:    # 1ra condicion. Funcion anidada(nested function).
        return x / n    # 2da condicion. Funcion que hace referencia a un valor de una funcion superior
    return division     # 3ra condicion. Funcion superior debe retornar la nested function.

def run():
    division_by_10 = make_division(10)
    print(division_by_10(5))

    division_by_20 = make_division(20)
    print(division_by_20(4))

    division_by_81 = make_division(81)
    print(division_by_81(9))

if __name__ == '__main__':
    run()
