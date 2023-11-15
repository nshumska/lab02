# Користувач вводить рік
year = int(input("Введіть рік: "))

# Перевірка чи високосний рік 
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year.")
else:
    print("Ordinary year.")
