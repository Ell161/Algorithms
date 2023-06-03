class MyTree:
    class Node:
        def __init__(self, value=None, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

        def get_value(self):
            return self.value

        def get_left(self):
            return self.left

        def get_right(self):
            return self.right

        def set_value(self, value):
            self.value = value

        def set_left(self, left):
            self.left = left

        def set_right(self, right):
            self.right = right

        def compare_to(self, data):
            if self.value == data:
                return 0
            elif self.value < data:
                return -1
            else:
                return 1

    def __init__(self):
        self.root = None

    def __add_node(self, current_node, value):
        new_node = self.Node(value)
        if current_node.compare_to(value) == 0:
            print(f'Узел({current_node.get_value()}) не был добавлен')
            return
        elif current_node.compare_to(value) > 0:
            if current_node.get_left() is None:
                current_node.set_left(new_node)
                print(f'Узел({current_node.get_value()}) + ({new_node.get_value()}) левый')
            else:
                self.__add_node(current_node.get_left(), value)
        else:
            if current_node.get_right() is None:
                current_node.set_right(new_node)
                print(f'Узел({current_node.get_value()}) + ({new_node.get_value()}) правый')
            else:
                self.__add_node(current_node.get_right(), value)

    def add(self, value):
        new_node = self.Node(value)
        if self.root is None:
            self.root = new_node
            print(f'Корневой узел({new_node.get_value()})')
            return
        self.__add_node(self.root, value)

    def __find_node(self, current_node, value):
        if current_node.compare_to(value) == 0:
            print(f'Узел({current_node.get_value()}) найден')
            return True
        elif current_node.compare_to(value) > 0:
            if current_node.get_left() is None:
                print('Обход дерева закончен. Узел не найден')
                return
            print(f'Идем влево, смотрим({current_node.get_left().get_value()})')
            self.__find_node(current_node.get_left(), value)
        else:
            if current_node.get_right() is None:
                print('Обход дерева закончен. Узел не найден')
                return
            print(f'Идем вправо, смотрим({current_node.get_right().get_value()})')
            self.__find_node(current_node.get_right(), value)

    def find(self, value):
        print(f'Смотрим корневой узел({self.root.get_value()})')
        return self.__find_node(self.root, value)

    def __find_min(self, current_node):
        if current_node.get_left() is None:
            return current_node
        return self.__find_min(current_node.get_left())

    def __remove_node(self, current_node, value):
        if current_node is None:
            return None
        if current_node.compare_to(value) > 0:
            # delete on the left branch
            current_node.set_left(self.__remove_node(current_node.get_left(), value))
            return current_node
        elif current_node.compare_to(value) < 0:
            # delete on the right branch
            current_node.set_right(self.__remove_node(current_node.get_right(), value))
            return current_node
        # if node is leaf
        if current_node.get_left() is None and current_node.get_right() is None:
            return None
        # if node has only one branch
        if current_node.get_left() is None and current_node.get_right() is not None:
            return current_node.get_right()
        if current_node.get_left() is not None and current_node.get_right() is None:
            return current_node.get_left()
        # if node has two branches
        smallest_node_on_the_right = self.__find_min(current_node.get_right())
        smallest_value_on_the_right = smallest_node_on_the_right.get_value()
        current_node.set_value(smallest_value_on_the_right)
        current_node.set_right(self.__remove_node(current_node.get_right(), smallest_value_on_the_right))
        return current_node

    def remove(self, value):
        self.root = self.__remove_node(self.root, value)

    # DFS (depth first search)
    # BFS (breath first search)
    def __dfs(self, current_node, result):
        # Pre-Order
        # result.append(current_node.get_value())
        if current_node.get_left() is not None:
            self.__dfs(current_node.get_left(), result)
        # In-Order
        result.append(current_node.get_value())
        if current_node.get_right() is not None:
            self.__dfs(current_node.get_right(), result)
        # Post-Order
        # result.append(current_node.get_value())

    def depth_first_search(self):
        if self.root is None:
            return None
        nodes_list = []
        self.__dfs(self.root, nodes_list)
        return nodes_list


my_tree = MyTree()
nodes = [5, 8, 13, 45, 3, 10, 4, 7, 23]
for node in nodes:
    my_tree.add(node)

my_tree.find(10)
my_tree.remove(13)
my_tree.find(10)

print(*my_tree.depth_first_search())
