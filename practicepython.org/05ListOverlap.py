# Take lists
# Get elements common in between lists (without duplicates)

def compare(list1, list2):
    common_num = []

    for i in list1:
        if i not in common_num:
            if i in list2:
                common_num.append(i)

    for j in list2:
        if j not in common_num:
            if j in list1:
                common_num.append(i)

    common_num.sort()

    return common_num

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(f"The common numbers between the two lists are {compare(a,b)}")