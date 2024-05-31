#!/usr/bin/env python3
# def hello():
#     print('Hello World')
#     print('Inside a Function')             #invistigation 1 part 1
#     return

# my_stuf = hello()
# print('Stuff return from hello(): ',my_stuf)
# print('the object my_stuff is of type: ',type(my_stuf))

# def return_text_value():
#     name = 'Terry'
#     greeting = 'Good Morning ' + name
#     return greeting                                     #invistigation 1 part 2

# text = return_text_value()
# print(text)

def return_number_value():
    num1 = 10
    num2 = 5
    num3 = num1 + num2
    return num3
number = return_number_value()
print('my number is', number)
print('my number is '+ str(number))
print('my number is '+ str(return_number_value()))

