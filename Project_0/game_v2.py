"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count = 1 # Как минимум будет 1 попытка
        lower_border=1 # нижняя граница граница интервала из которого выбирается случайное число
        upper_border=101 # верхняя граница граница интервала из которого выбирается случайное число
        predict_number = np.random.randint(lower_border, upper_border)  # предполагаемое число
        while True:
         count+=1
         if predict_number<number: #Если случайное число меньше искомого, то случайное число становится нижней границей диапазона поиска
             lower_border=predict_number
             predict_number = np.random.randint(lower_border, upper_border)
         if predict_number>number: #Если случайное число больше искомого, то случайное число становится верхней границей диапазона поиска
             upper_border=predict_number
             predict_number = np.random.randint(lower_border, upper_border)
         if number == predict_number:
             break  # выход внутреннего из цикла если угадали
        break # выход из внешнего цикла если угадали
    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
