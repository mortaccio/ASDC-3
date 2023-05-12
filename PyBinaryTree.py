class Node:
    def __init__(self, key, dish, cuisine, price):
        self.key = key
        self.dish = dish
        self.cuisine = cuisine
        self.price = price
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, dish, cuisine, price):
        if self.root is None:
            self.root = Node(key, dish, cuisine, price)
        else:
            self._insert_recursive(self.root, key, dish, cuisine, price)

    def _insert_recursive(self, node, key, dish, cuisine, price):
        if key < node.key:
            if node.left is None:
                node.left = Node(key, dish, cuisine, price)
            else:
                self._insert_recursive(node.left, key, dish, cuisine, price)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key, dish, cuisine, price)
            else:
                self._insert_recursive(node.right, key, dish, cuisine, price)

    def remove(self, key):
        self.root = self._remove_recursive(self.root, key)

    def _remove_recursive(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._remove_recursive(node.left, key)
        elif key > node.key:
            node.right = self._remove_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self._find_minimum(node.right)
                node.key = successor.key
                node.dish = successor.dish
                node.cuisine = successor.cuisine
                node.price = successor.price
                node.right = self._remove_recursive(node.right, successor.key)

        return node

    def _find_minimum(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node

        if key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    def preorder_traversal(self):
        self._preorder_recursive(self.root)

    def _preorder_recursive(self, node):
        if node is not None:
            print(f"Key: {node.key}, Dish: {node.dish}, Cuisine: {node.cuisine}, Price: {node.price}")
            self._preorder_recursive(node.left)
            self._preorder_recursive(node.right)

    def inorder_traversal(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if node is not None:
            self._inorder_recursive(node.left)
            print(f"Key: {node.key}, Dish: {node.dish}, Cuisine: {node.cuisine}, Price: {node.price}")
            self._inorder_recursive(node.right)

    def postorder_traversal(self):
        self._postorder_recursive(self.root)

    def _postorder_recursive(self, node):
        if node is not None:
            self._postorder_recursive(node.left)
            self._postorder_recursive(node.right)
            print(f"Key: {node.key}, Dish: {node.dish}, Cuisine: {node.cuisine}, Price: {node.price}")
        
file_name = 'data.txt'
bst = BinarySearchTree()

with open(file_name, 'r') as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()
    if line:
        key, dish, cuisine, price = line.split(',')
        bst.insert(int(key), dish, cuisine, float(price))

# Пример использования бинарного дерева поиска
print("Прямой обход:")
bst.preorder_traversal()

print("\nОбратныйтный обход:")
bst.postorder_traversal()

print("\nЦентрированный обход:")
bst.inorder_traversal()

# Пример поиска элемента
search_key = 5
result = bst.search(search_key)
if result is not None:
    print(f"\nНайден элемент с ключом {search_key}: Dish: {result.dish}, Cuisine: {result.cuisine}, Price: {result.price}")
else:
    print(f"\nЭлемент с ключом {search_key} не найден")

# Пример удаления элемента
remove_key = 10
bst.remove(remove_key)
print(f"\nЭлeмeнт с ключом {remove_key} удален")

print("\nOбновленный обход после удаления:")
bst.inorder_traversal()
