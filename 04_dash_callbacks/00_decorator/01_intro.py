"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

def dekorator(func):
    print('Python')
    return func


@dekorator
def hello_world():
    print('hello world')

hello_world()