class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList: # list, tuple, dict처럼 하나에 자료형을 만드는 것입니다!
    def __init__(self):
        init = Node('init')
        self.head = init
        self.tail = init
        self.count = 0

    def __len__(self):
        return self.count

    def __getitem__(self, index):
        current = self.head.next
        for _ in range(index):
            current = current.next
        return current.data

    def __str__(self):
        current = self.head.next
        result = ''
        for _ in range(self.count):
            result += f'{str(current.data)}, '
            current = current.next
        return f'<{result[:-2]}>'

    def __repr__(self):
        current = self.head.next
        result = ''
        for _ in range(self.count):
            result += f'{str(current.data)}, '
            current = current.next
        return f'<{result[:-2]}>'

    def append(self, data):
        new_node = Node(data)
        self.count += 1
        self.tail.next = new_node # 처음에는 Node('init').next
        self.tail = new_node

    def pop(self):
        if self.count == 0:
            raise IndexError('pop from empty list')
        last_node_data = self.tail.data
        current = self.head.next
        for _ in range(self.count):
            if current.next is self.tail:
                self.tail = current
                break
            current = current.next
        self.count -= 1
        return last_node_data
    
    def find(self, data):
        if self.count == 0:
            return -1
        current = self.head.next
        for i in range(self.count):
            if current.data == data:
                return i
            current = current.next
        return -1

###########################

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, data):
        init = Node(data)
        self.root = init
        self.count = 1
    
    def __len__(self):
        return self.count

    def insert(self, data):
        new_node = Node(data)
        current_node = self.root
        while current_node:
            if data == current_node.value: # 같은 데이터 만나면 넣어주지 않습니다!
                return
            elif data < current_node.value:
                if not current_node.left: # 왼쪽으로 갔더니 비어있는 경우!
                    current_node.left = new_node
                    self.count += 1
                    return
                current_node = current_node.left
            elif data > current_node.value:
                if not current_node.right: # 오른쪽으로 갔더니 비어있는 경우!
                    current_node.right = new_node
                    self.count += 1
                    return
                current_node = current_node.right