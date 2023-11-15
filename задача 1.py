# користувач вводить пять чисел
a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третє число: "))
d = int(input("Введіть четверте число: "))
e = int(input("Введіть п'яте число: "))

# Ініціалізуємо лічильник додатних чисел
positive_count = 0

# Перевіряємо кожне число і збільшуємо лічильник, якщо воно додатнє
if a > 0:
    positive_count += 1
if b > 0:
    positive_count += 1
if c > 0:
    positive_count += 1
if d > 0:
    positive_count += 1
if e > 0:
    positive_count += 1

# Виводимо результат
print("Кількість додатних чисел: ", positive_count)
