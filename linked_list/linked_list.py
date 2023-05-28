class LinkedList:
    class Node:
        def __init__(self, value=None, next=None):
            self.value = value
            self.next = next

        def get_value(self):
            return self.value

        def get_next(self):
            return self.next

        def set_value(self, value):
            self.value = value

        def set_next(self, next):
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        current_node = self.head
        output = ''
        while current_node is not None:
            output += str(current_node.get_value()) + ' -> '
            current_node = current_node.get_next()
        return output

    def get_head(self):
        return self.head

    def add(self, value):
        new_node = self.Node(value)
        current_node = self.head
        if current_node is None:
            self.head = new_node
            return
        while current_node.get_next() is not None:
            current_node = current_node.get_next()
        current_node.set_next(new_node)

    def add_start(self, value):
        new_node = self.Node(value)
        current_node = self.head
        new_node.set_next(current_node)
        self.head = new_node

    def remove_start(self):
        current_node = self.head
        if current_node is None:
            raise 'The list is empty!'
        else:
            self.head = current_node.get_next()

    def get_element(self, index):
        count = 0
        current_node = self.head
        if current_node is None:
            raise 'The list is empty!'
        while current_node is not None:
            if count == index:
                return current_node.get_value()
            count += 1
            current_node = current_node.get_next()
        raise 'Index is out of range!'

    def insert(self, index, value):
        new_node = self.Node(value)
        current_node = self.head
        count = 0
        if current_node is None:
            raise 'The list is empty!'
        while current_node.get_next() is not None:
            if index == 0:
                self.add_start(value)
                return
            elif count + 1 == index:
                node_after_current = current_node.get_next()
                current_node.set_next(new_node)
                new_node.set_next(node_after_current)
                return
            count += 1
            current_node = current_node.get_next()
        raise 'Index is out of range!'

    def remove(self, index):
        current_node = self.head
        count = 0
        if current_node is None:
            raise 'The list is empty!'
        while current_node.get_next() is not None:
            if index == 0:
                self.remove_start()
                return
            elif count + 1 == index:
                node_to_remove = current_node.get_next()
                node_after_removed = node_to_remove.get_next()
                current_node.set_next(node_after_removed)
                return
            count += 1
            current_node = current_node.get_next()
        raise 'Index is out of range!'

    # Homework
    def get_size(self):
        count = 0
        current_node = self.head
        if current_node is None:
            count = 1
            return count
        while current_node is not None:
            count += 1
            current_node = current_node.get_next()
        return count

    def pop(self):
        current_node = self.head
        if current_node is None:
            raise 'The list is empty!'
        while current_node.get_next().get_next() is not None:
            current_node = current_node.get_next()
        delete_element = current_node.get_next().get_value()
        current_node.set_next(None)
        return delete_element

    def reverse(self):
        previous = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.get_next()
            current_node.set_next(previous)
            previous = current_node
            current_node = next_node
        self.head = previous


my_list = LinkedList()
my_list.add(1)
my_list.add('dsfadgr')
my_list.add({3: 'aggtg'})
my_list.add([1, 2, 3, 4, 5])

print(my_list)
my_list.add_start(15)
print(my_list)

print(my_list.get_element(4))
my_list.insert(4, 'love coding')
print(my_list.get_element(4))

my_list.reverse()
print(my_list)
print(my_list.pop())
