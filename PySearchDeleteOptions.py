class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def display(self):
        for item in reversed(self.items):
            print(item)

# Чтение данных из текстового файла и создание стека
file_name = 'data.txt'
stack = Stack()
with open(file_name, 'r') as file:
    lines = file.readlines()
    for line in lines:
        data = line.strip().split(',')
        stack.push(data)

# Операции со стеком
print("Stack Contents:")
stack.display()

# Вставка элемента в стек
new_dish = ['32', 'Baked Salmon', 'American', '22.50']
stack.push(new_dish)
print("\nAfter Insertion:")
stack.display()

# Поиск элемента в стеке
search_dish = '7'
found = False
temp_stack = Stack()
while not stack.is_empty():
    item = stack.pop()
    if item[0] == search_dish:
        print(f"\nDish Found: {', '.join(item)}")
        found = True
        break
    temp_stack.push(item)

# Восстановление стека после поиска
while not temp_stack.is_empty():
    stack.push(temp_stack.pop())

if not found:
    print(f"\nDish with ID {search_dish} not found.")

# Удаление элемента из стека
delete_dish = '18'
found = False
temp_stack = Stack()
while not stack.is_empty():
    item = stack.pop()
    if item[0] != delete_dish:
        temp_stack.push(item)
    else:
        found = True
        print(f"\nDish Deleted: {', '.join(item)}")

# Восстановление стека после удаления
while not temp_stack.is_empty():
    stack.push(temp_stack.pop())

if not found:
    print(f"\nDish with ID {delete_dish} not found.")

# Окончательный вывод содержимого стека
print("\nStack Contents:")
stack.display()

