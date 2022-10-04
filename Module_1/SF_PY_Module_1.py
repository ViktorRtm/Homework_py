"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""
import numpy as np

"""Основной блок, в котором расчитывается среднее заначение
количества попыток угадывания числа, при n повторений
"""
def main ():
    n = 1000  #задаем, количество повторений
    sum_count = 0 #переменная для суммы попыток всех повторений
    i = 0

    """Считаем сумму всех попыток, каждый раз вызывая функкцию поиска числа,
    передавая в нее случайное число в диапазоне от 1 до 100
    """

    while i != n:
        sum_count = sum_count + random_predict(number=np.random.randint(1, 101))
        i += 1
    avr_count = sum_count/(n)
    print(avr_count)

"""Угадываем число бинарной сортировки
Args:
  number (int, optional): Загаданное число
Returns:
        int: Число попыток
"""
def random_predict(number:int) -> int:
    count = 0
    lst_num = np.array(range(1,101)) #создаем массив от 1 до 100
    while True:
        count += 1 #счетчик числа попыток
        predict_number = int(int(lst_num.sum())/int(lst_num.size)) #считаем 1ое предполагаемое число
        half = int(lst_num.size/2) #считаем переменную для создания нового массива
        """Проверяем в какой половине части массива находится загаданное число
           начиная с середины, потом справа, иначе - слева.
           Если справа то записываем массив от середины текущего массива и выше,
           если слева, то от середины текущего массива и ниже.
           Возвращаем число попыток
        """
        if predict_number == number:
            break
        elif predict_number < number:
            lst_num = lst_num[half:]
        else:
            lst_num = lst_num[:half]
        if int(lst_num.size) == 0:
            break
    return count

if __name__ == "__main__":
    main()
#%%
