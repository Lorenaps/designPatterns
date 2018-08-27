'''
    Decorator em python é uma função que permite extender uma outra função
    sem precisar modificar o código explicitamente.

    Ele é uma função que recebe outra função como parâmentro. E para
    utilizarmos é só colocar antes da função que vai ser decorada a notação
    @nome_do_decorator

    Atenção para o retorno do decorator
'''

import time

def timing_function(some_function):
    def wrapper():
        t1 = time.time()
        some_function()
        t2 = time.time()
        print("Time it took to run the function: " + str((t2 - t1)) + "\n")
    return wrapper

@timing_function
def my_function():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print("\nSum of all the numbers: " + str((sum(num_list))))

my_function()