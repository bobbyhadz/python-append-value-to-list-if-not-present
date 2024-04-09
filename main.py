# Append value to list if not already present using Python

my_list = [1, 2, 3, 4, 5]


value = 6

if value not in my_list:
    my_list.append(value)
else:
    print('The specified value is already present in the list')


print(my_list)  # 👉️ [1, 2, 3, 4, 5, 6]