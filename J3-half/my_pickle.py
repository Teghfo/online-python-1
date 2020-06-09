import pickle
import random
import os

path = '/home/ashkan/Desktop/Mapsa/'

# if not os.path.exists(path):
#     os.mkdir(path)

# os.chdir(path)

class Members:

    def read_data(self):
        self.name = input("Enter your Name: ")
        if not self.name:
            return
        self.id = random.randint(10**9, 10**10)
        self.email = input('Enter your mail: ')
        self.passw = input('Enter your pass: ')
        self.gire_rojin = ['as', (2, 2)]

    def print_mem(self):
        print(f'userid: {self.id}')
        print(f'name: {self.name}')
        print(self.gire_rojin)

f = open(path+'members', "wb")
mem_obj = Members()
mem_obj.read_data()

while mem_obj.name:
        pickle.dump(mem_obj, f)
        mem_obj.read_data()


f.close()


f = open(path+'members', "rb")

rojin = pickle.load(f)

while True:
    rojin.print_mem()

    try :
        rojin = pickle.load(f)

    except (EOFError) as err:
        print(f'tahe fili errotem ine: {err}')
        break

f.close()
    