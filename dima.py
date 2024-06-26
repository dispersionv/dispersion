# program.py
def get_last_element(lst):
    return lst[-1] if lst else None

# Запрос строки у пользователя и преобразование её в список
user_input = input("Введите значения через запятую: ")
values = user_input.split(',')
print("Последний элемент списка:", get_last_element(values))
