class node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None
class doubly_linkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head==None:
            print("Linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"<-->",end=" ")
                n=n.nref

    def display_rev(self):
        if self.head==None:
            print("Linked list is empty")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data,"<-->",end=" ")
                n=n.pref
    def add_begin(self,data):
        new_node=node(data)
        if self.head==None:
            self.head=new_node
        else:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node
    def add_end(self,data):
        new_node=node(data)
        if self.head is None:
            self.head = new_node
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.nref=new_node
            new_node.pref=n
    def add_after(self,data,x):
        if self.head==None:
            print("Linked list is empty")
        else:
            n=self.head
            while n is not None:
                if x==n.data:
                    break
                n=n.nref
            if n is None:
                print("Node is not Present")
            else:
                new_node=node(data)
                new_node.nref=n.nref
                new_node.pref=n
                if n.nref is not None:
                    n.nref.pref= new_node
                n.nref=new_node

    def del_begin(self):
        if self.head==None:
            print("Linked list is empty")
        if self.head.nref is None:
            self.head=None
        self.head=self.head.nref
        self.head.pref=None
    def del_end(self):
        if self.head==None:
            print("Linked list is empty")
        if self.head.nref is None:
            self.head=None
        n=self.head
        while n.nref is not None:
            n=n.nref
        n.pref.nref=None
    def search(self,x):
        n=self.head
        pos=1
        while n:
            if n.data==x:
                break
            n=n.nref
            pos+=1
        if n==None:
            print("data doesn't exist")
            return -1
        return pos

ll=doubly_linkedlist()
n1=node(9)
ll.head=n1
n2=node(77)
n1.nref=n2
n3=node(7)
n2.nref=n3
ll.add_begin(69)
ll.add_end(67)
ll.add_after(657,7)
ll.display()
print("After deleting")
ll.del_begin()
ll.display()
print("After deleting")
ll.del_end()
ll.display()