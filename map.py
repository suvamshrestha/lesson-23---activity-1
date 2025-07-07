list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
result_Add = list(map(lambda x, y: x + y, list1, list2))
print("addition of two lists:", result_Add)
list3 = [5, 6, 7, 8]
result_Square = list(map(lambda x: x ** 2, list3))
print("square of elements in list3:", result_Square)
