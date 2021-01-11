

class Node:

    def __init__(self, val):
        self.value = val
        self.link = None 

class LinkedList:

    def __init__(self):
        self.root = None

#   def printlist(self):
#       p = self.root
#       while(p.link != None):
#           print(p.value)
#           p = p.link
#       print(p.value)  #Don't forget about the last value

    def __iter__(self):
        self.position = self.root
        return self

    def __next__(self):
        if(self.position == None):
            raise StopIteration
        else:
            self.position = self.position.link
            return self.position.value

    def addafter(self):
        x = input('Valore da inserire nella lista: ')
        temp = Node(x)
        if(self.root == None):
            self.root = temp
        else:
            p = self.root
            while(p.link != None):
                p = p.link
            
            p.link = temp

myobject = LinkedList() #Created the list reference

#firstnode = Node(3)
#secondnode = Node(5)
#thirdnode = Node(7)

myobject.addafter()
myobject.addafter()
myobject.addafter()
for item in myobject:
    print(item)
