 #Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

 #Пример:

 #- 6 -> да
 #- 7 -> да
 #- 1 -> нет

num = int(input('Введите число '))

if num < 1 or num > 7 :
    print (" Некорректное число ")

if  num  < 6 :
    print (" Нет ")
else :
    print (" Да ")
