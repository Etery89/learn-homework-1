"""
Домашнее задание №1
Условный оператор: Сравнение строк
* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты
"""
str1 = 7906
str2 = 'learn' 

def main(str_1, str_2):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
  if isinstance(str_1, str) == True and isinstance(str_2, str) == True:
    if str_1 == str_2:
        return 1
    elif str_1 != str_2 and len(str_1) > len(str_2):
        return 2
    elif str_1 != str_2 and str_2 == 'learn':
        return 3
    else:
        return 4
  else:
    return 0  
    
if __name__ == "__main__":
    main(str1, str2)

# Текст моей программы. При помещении в шаблон ничего не работает. 
# Без шаблона всё ок 
# str1 = 7906
# str2 = 'learn'
# str3 = 'Congratulations'
# str4 = 'Python'
# str5 = 'Go'
# str6 = 'learn'
# str7 = 'Hello'
# str8 = 'Natalya Komarova'




# def str_comparison(str_1, str_2):
#     if isinstance(str_1, str) == True and isinstance(str_2, str) == True:
#         if str_1 == str_2:
#             return 1
#         elif str_1 != str_2 and len(str_1) > len(str_2):
#             return 2
#         elif str_1 != str_2 and str_2 == 'learn':
#             return 3
#         else:
#             return 4
#     else:
#         return 0    

# comparison_1 = str_comparison(str1, str2)
# print(comparison_1)
# comparison_2 = str_comparison(str3, str4)
# print(comparison_2)
# comparison_3 = str_comparison(str5, str6)
# print(comparison_3)
# comparison_4 = str_comparison(str7, str8)
# print(comparison_4)