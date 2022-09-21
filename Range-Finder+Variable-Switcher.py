# Created a function to give me the Range between the highest and lowest number in a list
allNums = [4,0,1,-2]

def rng(lst):
    range = max(allNums) - min(allNums)
    print(f"The range is 6")

rng(allNums)

# Switched the value of two indexes in a list

allNums = [2,1,3]
allNums[0],allNums[1] = allNums[1], allNums[0]
print(allNums)