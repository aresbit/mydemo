# type 'a list = Nil | Cons of 'a * 'a list
class Linked_List_Node:
	def __init__(self, x) -> None:
		self.item =  x
		self.next = None
	def later_node(self, i):
		if i == 0: return self 
		assert self.next
		return self.next.later_node(i - 1)

class Linked_List_Seq:
    def __init__(self) -> None:
        self.head = None
        self.size = 0
    def __len__(self) -> int:
        return self.size
    def __iter__ (self):
        node = self.node
        while node:
            yeild self.item
            node = node.next
    
    def build(self, A):
        for a in reversed(A):
            self.insert_first(a)
    def insert_first(self, x):
        self.head = Linked_List_Node(x, self.head)
        self.size += 1
    def get_at(self, i):
        assert i >= 0 and i < self.size
        return self.head.later_node(i).item
    def set_at(self, i, x):
        assert i >= 0 and i < self.size
        self.head.later_node(i).item = x
    def delete_first(self):
        assert self.size > 0
        self.head = self.head.next
        self.size -= 1

    def insert_at(self, i, x):
        assert i >= 0 and i <= self.size
        if i == 0:
            self.insert_first(x)
        else:
            self.head.later_node(i - 1).next = Linked_List_Node(x, self.head.later_node(i - 1).next)
            self.size += 1
    def delete_at(self, i):
        assert i >= 0 and i < self.size
        if i == 0:
            self.delete_first()
        else:
            self.head.later_node(i - 1).next = self.head.later_node(i - 1).next.next
            self.size -= 1
    def __str__(self):
        return str(self.to_list())
    def to_list(self):
        return [self.get_at(i) for i in range(self.size)]
    def __repr__(self):
        return str(self.to_list())
    
