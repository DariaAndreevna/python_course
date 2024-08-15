lst = [1, 2, 3, 4]

sum_el = 0
for i, el in enumerate(lst):
    if i % 2 == 0:
        sum_el = sum_el + el

x = lst[-1] if len(lst) != 0 else 0
result = sum_el * x
print(result)

# Спочатку пропустила, що у лекціях вже знайомили з sum, тому тримайте два варіанти :)

lst_2 = [1, 2, 3, 4]

even_el = []
for i, el in enumerate(lst_2):
    if i % 2 == 0:
        even_el.append(el)

x_2 = lst_2[-1] if len(lst_2) != 0 else 0
result_2 = sum(even_el) * x_2
print(result_2)
