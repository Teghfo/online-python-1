# data type
name = "ashkan"
age = 30
time = 20.5
is_active = True


# data casting
age = int("35")
# age = str(30)
print(name)

# data structure
mapsa_name = [10, 'ashkan', is_active, 10]  # list  --> mutable, start from zero index, similar array, iterable
mapsa_name_tuple = (10, 'ashkan', is_active) # tuple -- imutable
mapsa_name_set = {10, 'ashkan', is_active, 25} # set
mapsa_name_dictionary = {('ashkan','reza'): 912, 'negar':918, mapsa_name_tuple: 12}

mapsa_name_list_cast_tuple = tuple(mapsa_name)
mapsa_name_list_cast = set(mapsa_name)
mapsa_name_set_cast_list = list(mapsa_name_set)

print(mapsa_name_set_cast_list[1])
print(mapsa_name_dictionary[('ashkan','reza')])
## mapsaName  camelcase
## MapsaName  pascalcase

# mapsa_name_tuple[1] = 15
# print(mapsa_name)
# print(mapsa_name_tuple[1])
print(mapsa_name_list_cast)

# function
def mapsa_bootcamp(a , b):
    c = 1
    return a + b


# function input: index number in fibonachi series  1 , 1, 2 , 3 , 5, 8, 13 , .... output: value

def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        count = 2
        a , b = 1 , 1
        while count < n:
            a, b = b, a+b
            count += 1
        return b



#fibo_recursive(10) --> fibo_recursive(9) + fibo_recursive(8)
def fibo_recursive(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo_recursive(n-1) + fibo_recursive(n-2)

# print(fibo_recursive(100))


x = 10
y = 10


x = 11
# x = [1, 2]
# y= [1, 2]


print(id(x))
print(id(y))
# print(mapsa_bootcamp(10, 15))

# mapsa_name.append('mapsa')

# mapsa = mapsa_name.copy()   # deepcopy

# mapsa.append('bootcamp')


# print(mapsa_name)
# print(age)