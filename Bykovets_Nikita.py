#variant 3
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None


    # Добавление элемента в конец очереди
    def enqueue(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node


    # Удаление элемента из начала очереди
    def dequeue(self):
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return value


# Функция для получения простых множителей числа
def prime_factors(number):
    factors = []  # Список для хранения множителей
    divisors = [2, 3, 5]  # Множители для проверки
    for divisor in divisors:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
    return factors


# Функция для обновления очередей и нахождения минимального значения
def get_min_and_update_queues(queues, multipliers):
    # Получаем минимальные значения из очередей и удаляем их
    min_values = []
    for i in range(len(queues)):
        min_values.append(queues[i].dequeue())

    # Находим минимальное значение среди полученных
    min_value = min(min_values)

    # Обновляем очереди, добавляя в них новые значения
    for i in range(len(queues)):
        value = min_values[i]
        if value == min_value:
            # Если значение равно минимальному, добавляем в очередь произведение значения и множителя
            queues[i].enqueue(value * multipliers[i])
        else:
            # Иначе добавляем обратно удаленное значение
            queues[i].enqueue(value)
    return min_value


# Функция для вывода чисел с их множителями
def print_def(n):
    # Создаем пустой список для хранения очередей
    queues = []

    # Добавляем в список три пустые очереди
    for _ in range(3):
        queues.append(Queue())

    # Инициализируем очереди, добавляя в них множители 2, 3 и 5
    multipliers = [2, 3, 5]
    for i in range(len(multipliers)):
        multiplier = multipliers[i]
        queues[i].enqueue(multiplier)

    count = 1
    for l in range(n):  # Цикл для вывода n чисел
        min_value = get_min_and_update_queues(queues, [2, 3, 5])  # Получение минимального значения
        factors = prime_factors(min_value)  # Получение множителей
        print(f"{count}. {min_value}: {' '.join(map(str, factors))}")
        count += 1


# Обработка ввода пользователя и запуск функции
print("Эта программа выдает первые n натуральных чисел, в разложении которых на простые множители входят только числа 2,3,5")
while True:
    try:
        output = int(input("Введите число n: "))
        if output == 0:
            print("Введенное число не имеет множителей")
            break
        if output < 0:
            print("Число должно быть положительным")
        break
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое число.")

print_def(output)
