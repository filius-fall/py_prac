class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def insert(self,data):
        NewNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = NewNode
        else:
            self.head = NewNode

    def delrepeat(self):
        print('inside del')
        node = self.head
        if node is None:
            print('iniside forst id')
            return
        # while node.next is not None:
        #     if node == node.next:
        #         self.head = node.next.next
        print('SSSSSS')
        print(node.data)
        if node.data == node.next.data:
            while node.next.next:
                k = node.next
                if k == k.next:
                    print('KK')
                else:
                    print('BReak')
                
                node = node.next
        
            print(node.data)



llist = LinkedList()
first_node = Node(1)
llist.head = first_node
llist.insert(1)

llist.insert(2)
print(llist)

# def Solution(k):
#     print(k.data)
#     print(k.next)


llist.delrepeat()
print(llist)