# Write a function that takes a list value as an argument and returns 
# a string with all the items separated by a comma and a space, with 
# 'and' inserted before the last item.

# For example:
# Input: spam = ['apples', 'bananas', 'tofu', 'cats']
# Output: "apples, bananas, tofu, and cats"

list1 = ['bear', 'monkey', 'turtle', 'llama']
list2 = [5, 10, 15, 20, 25, 30, 35, 40]
list3 = [[1, 2], [3, 4], [5, 6], [7, 8]]
list4 = []
list5 = ["f"]

def convertToString(listArr):
    for i in range(len(listArr)):
        listArr[i] = str(listArr[i])

    if len(listArr) == 0:
        return listArr
    else:
        output = ", ".join(listArr)
    return output

print(convertToString(list1))
print(convertToString(list4))
print(convertToString(list5))
print(convertToString(list2))
print(convertToString(list3))