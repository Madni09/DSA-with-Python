class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

"""a = Node(1)
b = Node(2)
c = Node(3)

print(b.next)"""


class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n
    
    def insert_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

        self.n = self.n + 1

    def traverse(self):
        curr = self.head
        result = ''
        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next
        return result[:-2]
    
    """def append(self, value):
        new_node = Node(value)
        curr = self.head

        if curr.next is not None:
            curr = curr.next
            
            #you are at last node
            curr.next = new_node
            
        self.n += 1""" #the commendted code is not working, idk whyyy
    def append(self, value): #I got this  function from chatgpt😅
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head 
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
        self.n += 1

    def insert_after(self, after, value):
        new_node = Node(value)
        curr = self.head
        while curr != None:
            if curr.data == after:
                break
            curr = curr.next
#case 1 -> break, matlab hame item(after) mil gaya matlab curr ->(is) not none
        if curr != None:
            #logic
            new_node.next = curr.next
            curr.next = new_node
            self.n = self.n + 1
        else:
            return 'Item not found buddy'
        
#Now starts Algorithms to DELETE from a linked list:

    def clear(self):
        self.head = None
        self.n = 0
    
    def delete_head(self):
        if self.head == None:
            print('The linkedlist  is already empty')
        else:
            self.head = self.head.next
            self.n = self.n -1


    def pop(self):
        if self.head == None:
            return 'Empty LL'

        curr = self.head
        #ham puchh rahe hain ki kya LL me ek hi Node hai?
        if curr.next is  None:
            #matlab sirf Head hai apne pass.
            return self.delete_head()
        
        while curr.next.next != None:
            curr = curr.next
                # at this point, current is the 2nd last item(node) of the list
            curr.next = None
            self.n = self.n -1

    def remove(self, value):#this function deletes node by value
        if self.head == None:
            return 'Empty LL'

        if self.head.data == value: #do you want to remove the head node?
            return self.delete_head()
        
        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next
            #case 1 item mil gaya
            #case 2 item nahi mila
        if curr.next is None:
            return 'Not found'
        else:
                #case 1 item mil gaya
            curr.next = curr.next.next

#FROM HEAR, SEARCHING ALGORITHM STARTS FOR L.L:

    def search(self, item):
       
        curr = self.head
        pos = 0
        while curr!= None:
            if curr.data == item:
                return pos
            curr = curr.next
            pos = pos + 1

        #     print(f"{curr.data} Is in the L.L.")
        return 'not found yar'

    def __getitem__(self, index):
        curr = self.head
        pos = 0
        while curr != None:
            if pos == index:
                return curr.data
            pos = pos +1
            curr = curr.next
        return 'Index Error'
LL =  LinkedList()
LL.append(1)
LL.append(2)
LL.append(3)
LL.append(4)
LL.append(5)
#print(len(LL))

#LL.clear()
#LL.pop()
#a = LL.traverse()
#print(a)

"""f = LL.search(22)
print(f)"""

getitembyindex = LL[8]
print(getitembyindex)

#LL.remove(5)
#b = LL.traverse()
#print(b)

"""result = LL.insert_after(1, 200)
if result:
    print(result)"""






