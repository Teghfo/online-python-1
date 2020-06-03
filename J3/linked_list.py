###    elements -----> linked_list   ===>> methods     elm1 -> elm2 -> elm3 .... one directional linked_list

class Element:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.first = None
        
    def add_begin(self, elm):
        if self.first == None:
            self.first = elm
        else:
            elm.next = self.first
            self.first = elm


    def remove_elm(self, elm):
        
        if self.first == None:
            return
        elif self.first == elm:
            self.first = elm.next
            return 

        temp = self.first
        while temp != None:
            if temp.next == elm:
                temp.next = elm.next
                return
            temp = temp.next

        
    def print_list(self):
        if self.first == None:
            print('empty list')

        else:
            temp = self.first

            while temp != None:
                print(temp.data)
                temp = temp.next
            
    
    def add_between(self, elm, new_elm):
        pass

    def add_end(self):
        pass

    def count(self):
        pass

    def exist_elm(self, elm) -> bool:
        pass

    def find_index(self, elm) -> int:
        pass



if __name__=='__main__':
    lst = LinkedList()
    elm1 = Element('ashkan')
    elm2 = Element('ehsan')
    elm3 = Element('khal ghezi')


    lst.add_begin(elm1)
    lst.add_begin(elm2)
    lst.add_begin(elm3)

    lst.print_list()

    lst.remove_elm(elm3)


    print('\n\n')
    lst.print_list()


