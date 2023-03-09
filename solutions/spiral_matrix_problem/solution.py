from typing import List


class Solution(object):
    """
    Решение построенно на идеи рекурсии. Ф-ция заполняет все цифры на периметре
    и следом переходит к следубщему "слою" в котором так же заполняем все по периметру.
    Если визуализировать, то эта картина выглядела бы так.

    Например к нам пришла задача заполнить матрицу 6 Х 6
    Конечный результат должен выглядеть вот так:

     1  2  3  4  5  6
    20 21 22 23 24  7
    19 32 33 34 25  8
    18 31 36 35 26  9
    17 30 29 28 27 10
    16 15 14 13 12 11

    Не сложно написать алгоритм, который будет заполнять все цифры по контуру этой матрицы.
    Значит можно разбить заполнение по контурам, переходя от слоя к слою.
    Сначала заполняем внешний, следом переходим к внутреннему и так до самого конца. 

      1  2  3  4  5  6
     20              7      21 22 23 24
     19              8      32       25      33 34 
     18              9  ->  31       26  ->  36 35
     17             10      30 29 28 27
     16 15 14 13 12 11


    Первая цифра следующего контура будет равна: (Последнее число предыдущего уровня) + 1.
    Что бы выяснить какое число было последним можно либо запоминать его и передавать, либо прибегнуть к формуле:

    N * M - площадь или же самое большое число в этой матрице.
    (M - 2 * Layer) * (N - 2 * Layer) - площадь текущего. так как каждый внутренний квадрат
    становится меньше в высоту и в ширину на 2 числа.
    Выходит, что если мы из общей площади вычтем текущую, то получим как раз самое большое число, которое уже заполнили.

    Зная все то что выше, не сложно написать одну из реализаций. тут уж кому что нравится.
    """

    def spiral_matrix(self, n: int, m: int) -> List[List[int]]:
        res = []
        # Создаем матрицу и заполняем ее нулями. так как работаем по периметру,
        #   то нам необходимо подготовить весь массив перед заполнением
        for _ in range(n):
            new_l = [0] * m
            res.append(new_l)

        # считаем плозадь всего прямоугольника(кол-во всех элементов в матрице)
        sqare_area = n * m

        def filling_layer(lvl=0):
            """
            Ф-циф, которая будет заполнять матрицу по слоям
            """
            # считаем какое кол-во колонок и строк на данном слое
            column_count= m - lvl * 2
            row_count= n - lvl * 2
            # находим число с которого начинается данный слой
            current_num = sqare_area - row_count * column_count + 1

            # заполняем всю верхушку, кроме последнего символа
            for i in range(column_count-1):
                res[lvl][lvl + i] = current_num
                current_num += 1

            # заполняем весь правый ряд, кроме последнего символа
            for i in range(row_count-1):
                res[lvl + i][lvl + column_count - 1] = current_num
                current_num += 1

            # заполняем низ, кроме последнего
            for i in range(column_count-1):
                res[lvl + row_count - 1][lvl + column_count - 1 - i] = current_num
                current_num += 1

            # заполняем левый край, кроме последнего. Он у нас уже заполнен и равен начальному.
            for i in range(row_count-1):
                res[lvl + row_count - 1 - i][lvl] = current_num
                current_num += 1
            
            # Если текущий размер матрицы больше чем 2 по обеим из сторон, то мы еще не закончили.
            if column_count > 2 and row_count > 2:
                # увеличиваем слой и спускаемся ниже
                filling_layer(lvl + 1)

        filling_layer()
