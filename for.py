# """

# Домашнее задание №1

# Цикл for: Оценки

# * Создать список из словарей с оценками учеников разных классов 
#   школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
# * Посчитать и вывести средний балл по всей школе.
# * Посчитать и вывести средний балл по каждому классу.
# """

# def main():
#     """
#     Эта функция вызывается автоматически при запуске скрипта в консоли
#     В ней надо заменить pass на ваш код
#     """
#     pass
    
# if __name__ == "__main__":
#     main()

# _______________________________________________________________
# Задание "Цикл1":
numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

new_numbers = []

for number in numbers:
  number +=1
  print(number)
  new_numbers.append(number)

print(new_numbers)
# ________________________________________________________________
# Задание "Цикл2":
user_string = input('Введите строчку из вашей любимой песни:\n')

for symbol in user_string:
  print(f'{symbol}\n')

# _________________________________________________________________
# Задание "Оценки":
learners_scores = [{'school_class' : '5a', 'name subject': 'maths', 'scores' : [5, 3, 3, 4, 3, 5, 5, 4, 3, 5 ]}, 
                   {'school_class' : '6b', 'name subject': 'literature', 'scores' : [3, 3, 3, 2, 3, 3, 5, 4, 3, 4 ]}, 
                   {'school_class' : '7v', 'name subject': 'english language', 'scores' : [4, 4, 3, 4, 5, 5, 5, 4, 3, 3 ]}, 
                   {'school_class' : '7g', 'name subject': 'history', 'scores' : [5, 5, 5, 5, 2, 5, 5, 5, 5, 5 ]}
                  ]

sum_all_class = 0

for index_list in learners_scores:
  name_class = index_list['school_class']
  value = index_list['scores']
  print(value)
  av_sum_class = sum(value)/len(value)
  print(f'Средняя оценка по классу {name_class}: {av_sum_class}')
  sum_all_class += av_sum_class
  print(sum_all_class)

sum_all_school = sum_all_class/len(learners_scores)
print(f' Средняя оценка по школе: {sum_all_school}')