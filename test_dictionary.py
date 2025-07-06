test_dict = { "codingal":3, "is":2, "best":2, "for":2, "coding":1}
print("testdictionary", test_dict)
word = input("enter the word to check the frquency:")
if word in test_dict:
    print("the frequency of the word is:", test_dict[word])
else:
    print("the frequency of the word is not present in the dictionary")