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
            nodes.append(node.data)
            node = node.next
        return '->'.join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self,node):
        node.next = self.head
        self.head = node

    def add_last(self,node):
        if self.head is None:
            self.head = node
            print('HEYYYYYY')
        for i in self:
            pass
        print(node)
        i.next = node

    def add_after(self,target_node,next_node):
        if self.head is None:
            raise Exception('Link doesnt exist')

        for node in self:
            if node.data == target_node:
                next_node.next = node.next
                node.next = next_node
                return

        raise Exception('Node data not found')


llist = LinkedList()



first = Node('A')
llist.head = first


second = Node('B')
third = Node('c')

first.next = second
second.next = third





llist.add_first(Node('0'))

llist.add_last(Node('C'))

llist.add_after("c",Node('KK'))

print(llist)