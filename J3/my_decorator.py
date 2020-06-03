def my_decorator(*args, director = None , **kwargs):
    print(args, kwargs)

    def outer_function(func):
        def wrapper(*args , **kwargs):
            pass
            result = director

            if args[0] == 'ashkan':
                result = func(args[0])
            else: 
                print('not hero')

            if kwargs:
                print(kwargs)

            return result
        return wrapper
    return outer_function



# @decorator2
@my_decorator(director = 'nolan')
def print_hello(name):
    print(f'{name} is hero')
    return 'Nolan'


# print_hello = decorator2(my_decorator(print_hello))

print_hello('joker', actor= 'heath leacher')
print(print_hello('joker'))
