
import math
import random
from time import sleep

repeat = 'да'

#генератор квадратных уравнений
def generator():
    #Переменные
    n = 1
    k = 0
    a = 0
    n1 = 0
    l = 0
    b = 0
    c = 0
    D = 0
    x1 = 0
    x2 = 0
    x = 0
    z = 0
    print('Вы запустили программу для генерации примеров квадратного уравнения!')
    sleep(1)
    #Сам генератор
    while z != 1:
        #Запрос данных
        print('Сколько примеров вам сгенерировать?')
        sleep(1)
        k = int(input('Мне сгенерировать: '))
        sleep(1)
        print('Сколько максимально должно быть примеров с ответом "корней нет"?')
        sleep(1)
        n = int(input('Должно быть: '))
        sleep(1)
        if k < n or k < 0 or n < 0:
            print('Ошибка: вы ввели несуществующие варианты!')
            sleep(1)
        else:
            z = 1

    print("Ваши примеры с ответами:")
    sleep(1)

    #Сам алгоритм для поиска частных случаев и их решения
    while k!=l:
        a = random.randint(-20,20)
        if a == 0:
            a=1
        b = random.randint(-20,20)
        c = random.randint(-20,20)
        D = (b**2) - (4*a*c)
        if D > 0 :
            x1 = (-b + math.sqrt(D))/(2*a)
            x2 = (-b - math.sqrt(D))/(2*a)
            if x1 == int(x1) and x2 == int(x2):
                if b >=0:
                    if c >= 0:
                        print ( "f(x)={}x^2+{}x+{}=0".format(a,b,c) )
                    else:
                        print ( "f(x)={}x^2+{}x{}=0".format(a,b,c) )
                else:
                    if c >= 0:
                        print ( "f(x)={}x^2{}x+{}=0".format(a,b,c) )
                    else:
                        print ( "f(x)={}x^2{}x{}=0".format(a,b,c) )
                print("D =",D)
                print ("Ответ: x1 =", int(x1) ,"\n       x2 =", int(x2))
                sleep(1)
                print("---------------------------------")
                sleep(1)
                l+=1
            else:
                pass
        elif D == 0:
            x = -b / (2 * a)
            if float(x) == int(x):
                if b >=0:
                    if c >= 0:
                        print ( "f(x)={}x^2+{}x+{}=0".format(a,b,c) )
                    else:
                        print ( "f(x)={}x^2+{}x{}=0".format(a,b,c) )
                else:
                    if c >= 0:
                        print ( "f(x)={}x^2{}x+{}=0".format(a,b,c) )
                    else:
                        print ( "f(x)={}x^2{}x{}=0".format(a,b,c) )
                print("D =",D)
                print("Ответ: x =", int(x))
                sleep(1)
                print("---------------------------------")
                sleep(1)
                l+=1
            else:
                pass
        elif D < 0:
            if n1 < n:
                print ( "f(x)={}x^2+{}x+{}=0".format(a,b,c) )
                print("D =",D)
                print("Ответ: корней нет")
                sleep(1)
                print("---------------------------------")
                sleep(1)
                l+=1
                n1+=1
        else:
            pass

#Калькулятор квадратных уравнений 
def decision():
    print('Вы запустили программу для решения квадратных уравнений.')
    sleep(1)
    print("Формула квадратного уравнения: ax^2+bx+c=0")
    sleep(1)
    a = int(input('Введите а: '))
    b = int(input('Введите b: '))
    c = int(input('Введите с: '))
    D = b**2 - 4*a*c
    if D>0:
        x1 = str((-b + math.sqrt(D))/(2*a))
        x2 = str((-b - math.sqrt(D))/(2*a))
        print('2 корня: х1 = '+ x1 +' \n         x2 = '+x2)    
    elif D == 0:
        x1 = str(-b/(2*a))
        print('1 корень, х= '+x1)
    elif D<0:
        print('Дискриминант меньше нуля, корней нет')

print('Данная программа может генерировать и решать квадратные уравнения!') 
sleep(1)
#Алгоритм для работы программы
while repeat == 'да':
    choice = 3
    
    while choice < 0 or choice > 2 :
        print('Введите цифру 1 если хотите,чтобы программа сгенерировала вам квадратные уравнения с ответами!')
        sleep(1)
        print('Введите цифру 2 если хотите решить квадратное уравнение!')
        sleep(1)
        choice = int(input('Мой ответ: '))
        sleep(1)
        if choice <= 0 or choice > 2:
            print('Ошибка: вы ввели несуществующий вариант ответа!')
            sleep(1)
    if choice == 1:
        generator()
    if choice == 2:
        decision()
    sleep(1)
    k = 0
    while k != 1:
        print('Хотите ли вы заново запустить программу?(да/нет)')
        repeat = str(input('Мой ответ: '))
        repeat.replace(' ', '')
        repeat.lower()
        sleep(1)
        if repeat == 'да':
            k = 1
        elif repeat == 'нет':
            k = 1
        else:
            print('Ошибка: вы ввели несуществующий вариант ответа!')
            sleep(1)
        
    
print('Программа закончила свою работу. Спасибо за использование данной программы! Эту программу создал Кирилл Сухоруков!')
input()