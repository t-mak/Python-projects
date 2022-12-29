def sort_helper(given_array):
    print()
    print("Sorting an array: " + str(given_array))
    sorted_array = sort_array(given_array)
    print("Sorting result: " + str(sorted_array))

def sort_array(given_array):
    length_array = len(given_array)
    while (length_array>1):
        swapped = False
        for j in range(0, length_array-1):
            if given_array[j] > given_array[j+1]:
                temp = given_array[j]
                given_array[j] = given_array[j+1]
                given_array[j+1] = temp
                swapped = True
        length_array = length_array - 1 #since the highest value element is put at the end of the list each turn, no need to check it (2nd turn, means last 2 elements are sorted, 3rd turn means 3 last elemenets are sorted for sure etc.)
        if not swapped:
            break
    return given_array

array1 = [3, 1, 5, 7, 2, 4, 4, 4, 9, 8, 7]
array2 = [1560, 3410, 10, 2033]
array3 = [3, -10, 15, -93, 1, -13, 5]
sort_helper(array1)
sort_helper(array2)
sort_helper(array3)



