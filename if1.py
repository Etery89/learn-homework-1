"""
Домашнее задание №1
Условный оператор: Возраст
* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран
"""
age_user = input('Пожалуйста введите свой возраст:\n')

def main(age):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    if age != '':
        age = int(age)
        if 0 <= age <=2:
            return 'Вам еще рано в сад. Сидите дома с мамой!'
        elif 3 <= age < 7:
            return 'Вы посещаете дошкольное учебное заведение :)'
        elif 7 <= age <= 17:
            return 'Да вы уже школьник XD'
        elif 18 <= age <= 23:
            return 'Студент, не прогуливайте лекции!'
        else:
            return "Если вы еще не работаете, то пора начинать!"
    else:
        return 'Неверный формат ввода'

if __name__ == "__main__":
    main(age_user)

# # Вот моя программа. Отдельно от скрипта она работает. 
# Однако когда я помещаю внутрь шаблона 
# даже просто функцию определения активности, то ничего не работает.(см выше)
# age_user = input('Пожалуйста введите свой возраст:\n')

# def selection(age):
#     if age != '':
#         age = int(age)
#         if 0 <= age <=2:
#             return 'Вам еще рано в сад. Сидите дома с мамой!'
#         elif 3 <= age < 7:
#             return 'Вы посещаете дошкольное учебное заведение :)'
#         elif 7 <= age <= 17:
#             return 'Да вы уже школьник XD'
#         elif 18 <= age <= 23:
#             return 'Студент, не прогуливайте лекции!'
#         else:
#             return "Если вы еще не работаете, то пора начинать!"
#     else:
#         return 'Неверный формат ввода'


# def format_input(input_user):
#     input_user = input_user.split(' ')
#     input_user =''.join([str(elem) for elem in input_user])
#     if input_user.isalpha() == False:
#         if input_user.isdigit() == True:
#             age_int = selection(input_user) 
#             return age_int
#         else:
#             input_user = float(input_user)
#             age_float = selection(input_user)
#             return age_float
#     else:
#         return 'Введите число цифрами'

# your_activity = format_input(age_user)
# print(your_activity)