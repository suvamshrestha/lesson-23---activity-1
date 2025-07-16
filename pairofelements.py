class pairfinder():
    def find_pair(self, nums, target):
        lookup = {}
        for i , num in enumerate (nums):
            if target - num in lookup:
                return lookup[target - num], i
            lookup[num] = i
        return "no pair found"
target = int(input("Enter the target number: "))
nums = (10,20,30,40,50,60,70)
result = pairfinder().find_pair(nums, target)
print("indices of the pair are: ", result)
