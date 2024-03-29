'''
Декораторы
'''
'''
1) Преобразовать в верхний регистр текст которую возвращает функция
не изменяя код функции применяя декоратор
'''
# def make_upper_text(func):
#     def wrapper():
#         result = func()
#         return result.upper()
#     return wrapper

# @make_upper_text
# def get_text():
#     return 'hello world'

# print(get_text())
'''
2) Функция 
'''

# def cypher_number(func):
#     def wrapper():
#         phone_number = func()
#         cypher_num = ''
#         for i, d in enumerate(phone_number):
#             if i in (0, 1, 2):
#                 cypher_num += d
#             elif i in (10, 11):
#                 cypher_num += d
#             else:
#                 cypher_num += '#'
#         return cypher_num
#     return wrapper


# @cypher_number
# def get_number():
#     return '996220000018'

# print(get_number())
'''
3) Напишите декоратор, выводящий приветствие перед выполнением функции
'''

# def greeting(func):
#     def wrapper():
#         print('Hello!')
#         result = func()
#         return result
#     return wrapper

# @greeting
# def get_number():
#     return '996220000018'

# print(get_number())
'''
4) напишите декоратор удваивающий результат функции
'''
# def double_salary(func):
#     def wrapper():
#         result = func()
#         return result * 2
#     return wrapper

# @double_salary
# def get_salary():
#     salary = 50000
#     return salary

# print(get_salary())
'''
5) декоратор печатающий смс после выполнения функции
'''
# def print_notification(func):
#     def wrapper():
#         result = func()
#         print('Вам начислили зарплату')
#         return result
#     return wrapper

# @print_notification
# def get_salary():
#     salary = 50000
#     return salary

# get_salary()
'''
6) Декоратор для измерения времени выполнения функции:
Напишите декоратор который измеряет время выполнения функции и выводит результат.
'''
import time

def timer_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f'Время заняло: {end_time - start_time} секунд')

    return wrapper

@timer_decorator
def send_message_to_users():
    users = range(1, 1000001)
    for user in users:
        print(f'Отправка сообщения пользователю{user}')

send_message_to_users()