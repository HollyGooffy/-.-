
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None


    # Функция добавления элемента в конец очереди
    def enqueue(self, value):
        new_node = Node(value)  # Создаем новый узел
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node


    # Функция удаления элемента из начала очереди
    def dequeue(self):
        if self.head is None:  # Если очередь пуста
            return None
        value = self.head.value  # Сохраняем значение головы очереди
        self.head = self.head.next  # Перемещаем голову очереди на следующий узел
        if self.head is None:
            self.tail = None  # Устанавливаем хвост очереди в None
        return value


# Функция для вывода первых n натуральных чисел
def print_numbers(n):
    if n <= 0:
        print("Ошибка: Количество чисел должно быть положительным.")
        return  # Завершаем функцию

    x2 = Queue()  # Создаем очередь для чисел, кратных 2
    x3 = Queue()  # Создаем очередь для чисел, кратных 3
    x5 = Queue()  # Создаем очередь для чисел, кратных 5
    unumbers = {1}  # Список уникальных чисел

    x2.enqueue(2)  # Добавляем начальные значения в очереди
    x3.enqueue(3)
    x5.enqueue(5)

    print("первые",n,"чисел, в разложении которых на простые множители входят только числа 2, 3 и 5:")

    count = 1
    for i in range(n):  # Цикл для вывода чисел
        next_number = min(x2.head.value, x3.head.value, x5.head.value)  # Находим минимальное значение

        print(f"{count}. {next_number}")
        count += 1

        if next_number == x2.head.value:  # Если число совпадает с головой очереди x2
            x2.dequeue()  # Удаляем его из очереди
        if next_number == x3.head.value:
            x3.dequeue()
        if next_number == x5.head.value:
            x5.dequeue()

        # Добавляем кратные числа в очереди, если они еще не присутствуют
        if next_number * 2 not in unumbers:
            x2.enqueue(next_number * 2)
            unumbers.add(next_number * 2)
        if next_number * 3 not in unumbers:
            x3.enqueue(next_number * 3)
            unumbers.add(next_number * 3)
        if next_number * 5 not in unumbers:
            x5.enqueue(next_number * 5)
            unumbers.add(next_number * 5)

    print()


# Результат
print("Эта программа выдает первые n натуральных чисел, в разложении которых на простые множители входят только числа 2,3,5")
while True:
    try:
        n = int(input("Введите число n: "))
        break
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое число.")

print_numbers(n)
