"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

def dekorator(func):
    def wrapper():
        func()
        print('Wywołanie funkcji wrapper')
    return wrapper

@dekorator
def func_2():
    print('Wywołanie func_2')
    
func_2()