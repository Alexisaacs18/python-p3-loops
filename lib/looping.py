#!/usr/bin/env python3

def happy_new_year(num=10):
    while num > 0:
        print(num)
        num -= 1
    return print("Happy New Year!")


happy_new_year()


def square_integers(int_list):
    new_int_list = [x ** 2 for x in int_list]
    return new_int_list


print(square_integers([-1, -2, -3, -4, -5]))


def fizzbuzz():
    i = 1
    while i < 101:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        i += 1


fizzbuzz()
