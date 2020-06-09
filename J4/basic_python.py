################### operator ################

#arithmatic operator
# + , -, *, / (5/2 = 2.5), % (5%2 = 1), 5//2 = 2, ** (2**3 = 8) power


#1   **
#2   * / // %    (most left)
#3   + -

x = 2+3%2*4+(5**(2+1))
# print(x)

# comparision operator  
# < > <= >= != (not equal) ==

# print( '10 > 5: ', 10>5 , '10 == 15: ',  10==15 )

# print('5' == 5)

# #boolean
# # not (naghiz)  and ( True and True = True)  or (False or False = False)

# print(not '5' == 5)


# print( False or False)

# #   5&2
# # 5 = 101 & 010 = 000

# # 9 = 1001  12 = 1100  
# print(9&12)

# print(9 | 12)    # 1101 = 1 + 4 + 8

# print(19>>3)   # 101 --> 001  (taghsim be 2 be tedad shift rast)

# print(5<<2)    #  101 ---> 10100 ( x << y    x * y** 2)

# print(~5)    # 101 ==> 010
# print(~(-6))

# print(~7)

# # print ('g' in 'ashkan')
# print(6 in [2,6,7])
# print('ashkan1' in {'ashkan': 91})

#1  not
#2 arithmatic operator
#3 shift operator
#4 < >
#5 == !=

# print('ashkan ' + 'soghra')







###########################  function #####################


#    input(nagire)  -------> func -------> output(nagire)

def sakineh(age):
    print(['shovar nimikonam', 'shovar mikonam'][ age < 28])   # 25 ---> 1  tuple[1]
    # ternary operator    statement ? a:b    age<28 ? 'shovar mikonam':'shovart nemikonam'

# sakineh(29)


def print_hello(*name, **kwargs):
    print(name)
    print(kwargs)
    if name:
        print(f'hello {name[0]}')
    else:
        print('hello har ki hasi')



def ghorekishi_khodro(rant, name = 'dalal'):
    if name == 'dalal' or rant:
        print('barandeh shodi')
    else:
        print('boro peye zendegit')



def BMI(weight, height):
    bmi = weight / (height**2)

    return bmi

print(BMI(120, 1.70))

# print_hello('arta', 'ashkan', 'benyamin', khananende = 'Haydeh')
# ghorekishi_khodro(True, 'mojtaba')

#######  if/else    while    for


'''
age = 41
if age < 28:
    print('shovar mikonam')
else:
    print('shovar nimikonam')

if age< 28:
    print('shovar mikonam')
elif 28<age<30:
    print('maliat bede bad shovar')
elif 30<age<40:
    print('mehramam aval migiram shovar mikonam')
else:
    print('dari mimiri')
'''

mapsa_python = ['E', 'A', 'M', 'Z', 'N', 'ER']

'''
for name in mapsa_python:
    greetng = 'welcome ' + name
    if name == 'A':
        # mapsa_python.remove(name)
        # mapsa_python.remove('M')
        continue     #break
    print(greetng)
'''

phone_num = {'ashkan': 918, 'arta': 917, 'Eil': 912}


# unpacking
# a, b = ('ashkan', ('asghar', 'bahman'))

# print(a, b)

# for key, value in phone_num.items():
#     print(f'{key} phone num:  {value}')


# print(mapsa_python)





########  local vs global variable ########

x = 10

my_list = [1, 2]

def f():
    # global x
    x = 12   ###local
    my_list.append(10)


f()
# print(my_list)

## call by refrence -----> list - tuple - dictionary - objects - .... ,   call by value  -------> int, float, string, boolean



print('hasan gholi')

######   module, pakage

### *.py -----> module 

print(__name__)


if __name__ == '__main__':
    print('mojtaba.m base rant khari')


####### class