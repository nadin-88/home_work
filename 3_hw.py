#2. Функция на вход получает два произвольных числа. Вывести в консоль наибольшее из чисел.
        def biggest_number (a,b):
            if a > b:
                print(a)
            elif b > a:
                print (b)
        biggest_number(25, 46)


#3 Функция на вход получает два произвольных числа. Вывести в консоль “yes”, если они отличаются друг от друга на 135, иначе вывести на экран “No”
        def num_difference(a,b):
            if (a-b) == 135:
                print( 'Yes')
            else:
                print('No')
        num_difference(271,136)


#4. Функция на вход получает произвольное число от 1 до 12 (номер месяца). Вывести название сезона года в консоль (зима, весна, лето, осень)
        def seasons(month_number):
            if month_number == 12 or month_number == 1 or month_number == 2:
                print( 'Зима')
            elif month_number in range(3,6):
                print('Весна')
            elif month_number in range (6,9):
                print('Лето')
            elif month_number in range (9, 12):
                print('Осень')
        seasons(7)


#5.Функция на вход получает три произвольных числа. Если все числа больше 10, то вывести на экран “yes”, иначе “no”;
def equal_difference(a, b, c):
    if a>10 and b>10 and c> 10:
        print('Yes')
    else:
        print('No')
equal_difference(11,25,6)


#6. Функция на вход получает список, состоящий из 5 произвольных чисел. Найти количество положительных чисел среди них.
def count_positive_numbers(numbers):
    return sum(1 for num in numbers if num >0)
numbers_list =[1, 56, -5, 0, 89]
print(count_positive_numbers(numbers_list))

