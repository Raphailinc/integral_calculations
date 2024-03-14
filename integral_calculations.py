import numpy as np
import math

def make_array(N):
    print("Число элементов:",N)
    y0 = 0.84616823
    k = 8
    sequence = [y0]  # массив псевдослучайных чисел
    for i in range(N - 1):  # метод середины квадратов
        val = sequence[-1] ** 2
        fractional, _ = math.modf(val * 10 ** (k // 2))
        next_val = int(fractional * 10 ** k) * 10 ** (-k)
        sequence.append(next_val)
    return sequence
    
#новый массив для первого интеграла
def new_array1(sequence):
    return [math.sqrt(2 * y) for y in sequence]
    
#новый массив для второго интеграла
def new_array2(sequence):
    return [(2 * y) for y in sequence]
    
def calcI1():
    I1=0#вычисление интеграла по плотности x
    for i in range (N):
        I1+=new_sequence1[i]**(-0.25)
    I1=I1/N#M1
    print("I1=", I1)
    D1=0#дисперсия 1
    d=0
    for i in range (N):
        d+=new_sequence1[i]**(-0.5)
    D1=d/N-I1**2
    print("D1=", D1)
    E1=((D1 / N) ** 0.5)
    print("E1=", E1)

def calcI2():
    I2=0#вычисление интеграла по плотности 1/2
    for i in range (N):
        I2+=new_sequence2[i]**0.75
    I2=I2*2/N#M2
    print("I2=", I2)
    D2=0#дисперсия 2
    d=0
    for i in range (N):
        d+=new_sequence2[i]**1.5
    D2=d*4/N-I2**2
    print("D2=", D2)
    E2=2 * ((D2 / N) ** 0.5)
    print("E2=", E2)
    
N = 500  # число элементов
num_bins = 14  # кол-во интервалов
sequence = make_array(N)
new_sequence1 = new_array1(sequence)
new_sequence2 = new_array2(sequence)

calcI1()
calcI2()