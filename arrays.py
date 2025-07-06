import array as arr
array = arr.array('i', [1, 3, 5, 3, 7, 9, 3])
print("original array", array)
print("count of 3 in array:", array.count(3))
array.reverse()
print("reversed array:", array)
