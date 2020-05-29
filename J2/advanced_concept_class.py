########################## metaclass vs inheritance #############

# # every class in python a object of metaclass 

# class Person:
#     pass


# class Meta(type):
#     def print_hello(self):
#         print('in meta')




# # all class in python is subclass object
# # all keyword class is object of metaclass 



# # __new__ , __init__  ,   __call__
##   create instance of class ===> __new__(cls) [classmethod that create instance of class]  -----> __init__(self) [constructor initialize state]

# class Child(Person, metaclass=Meta):
#     def print_child(self):
#         print('in class Child')




# class ChildChild(Child):
#     pass



# c = ChildChild()
# # c.print_hello()


# class A: 
#     def print_hello(self):
#         print('in class A')

# class B(A):
#     pass

# b = B()
# b.print_hello()

# # print('child is instance Person: ', isinstance(Child, Person))
# # print('child is subclass Person: ', issubclass(Child, Person))


# # def Mapsa():
# #     pass

# # print(type(Mapsa))

# # print('fun is instance type: ', isinstance(Mapsa, type))

# # # A -> B -> C object of C

# # print(isinstance(Person , type))

# # print('type is subclass object: ', issubclass( type, object))
# # print('object is subclass type: ', issubclass(object, type))


# # print('object is instance type: ', isinstance(object, type))
# # print('type is instance object: ', isinstance(type, object))


# # print(issubclass(Person, object))



#  instance  ====> (state local ---> property , method)  , state global ===> class property

## OOP  ---> DesignPattern  (creational, structural, behavioral) ===>  GoF  1995 design pattern c++ , 23 designpattern
# ## singleton ====> class singleton ===>  unique instance

# ####################### static method , class method, object method #############
# class MapsaExample:

#     count =0
#     _instance = None

#     def __init__(self, name):
#         self.name = name
#         MapsaExample.count+=1

    
#     # def __new__(cls, name):
#     #     print(name)
#     #     if not cls._instance:
#     #         cls._instance = super().__new__(cls)
#     #     return cls._instance


#     def print_hello(self):
#         print(f'hello {self.name}')

#     # @classmethod
#     # def my_class_method(cls, name):
#     #     if cls.count < 3:
#     #         temp = cls.__new__(cls)
#     #         temp.__init__(name)
#     #         return temp

#     @staticmethod
#     def my_static(age, self=None):
#         if self:
#             print(f'hello in static {self.name}')

#         print(f'hello in static {age}')

# obj1 = MapsaExample('ashkan')
# obj2 = MapsaExample('asghar')
# # obj3 = MapsaExample.my_class_method('akbar')

# # print(obj3.name)


# print()

# # obj1.my_static(25, self=obj1)
# # MapsaExample.my_static(12)
# # MapsaExample.print_hello(obj2)

# # obj1.my_class_method()

# print(id(obj1))
# print(id(obj2))

# print(obj1.name)
# print(obj2.name)

class Graph:
    def __init__(self):
        self.adjMat = {}

    def add_node(self, node):
        if node not in self.adjMat.keys():
            self.adjMat[node] = []

    
    def add_edge(self, node1, node2):
        if node1 in self.adjMat.keys() and node2 in self.adjMat.keys():
            if node1 in self.adjMat[node2]:
                return
            else:
                self.adjMat[node1].append(node2)
                self.adjMat[node2].append(node1)
        
        else:
            print(f'{node1} or {node2} not exist')

    def print_graph(self):
        print(self.adjMat)


    def remove_node(self, node):
        pass

    def remove_edge(self, node1, node2):
        pass

    def is_connected(self):
        pass

    def shortest_path(self, node1, node2):
        pass


g = Graph()
g.print_graph()

g.add_node('a')
g.add_node('b')
g.add_node('c')
g.add_node('d')

g.add_edge('a', 'b')
g.add_edge('a', 'c')
g.add_edge('a', 'b')
g.add_edge('a', 'j')

g.print_graph()    