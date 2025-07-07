list1 = [1, 2, 3]
list2 = [7, 6, 5]
list3 = list(zip(list1, list2))
print(list3)  # Output: [(1, 7), (2, 6), (3, 5)]
for x , y in zip(list1, list2[::-1]):
    print(x, y)  
new_Dict = {list1: list2 for list1, list2 in zip(list1, list2)}
print(new_Dict)  # Output: {1: 7, 2: 6, 3: 5}    