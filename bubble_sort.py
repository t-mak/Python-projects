
given_array = [3, 1, 5, 7, 2, 4, 4, 4, 9, 8, 7]

length_array = len(given_array)
turn = 0

while (length_array>1):
    swapped = False
    turn = turn + 1
    for j in range(0, length_array-1):
        if given_array[j] > given_array[j+1]:
            temp = given_array[j]
            print()
            print("While loop iteration: " + str(turn))
            print("Swapping " + str(given_array[j]) + " with " + str(given_array[j+1]))
            given_array[j] = given_array[j+1]
            given_array[j+1] = temp
            print(given_array)
            swapped = True
    length_array = length_array - 1 #since the highest value element is put at the end of the list each turn, no need to check it (2nd turn, means last 2 elements are sorted, 3rd turn means 3 last elemenets are sorted for sure etc.)
    if swapped == False:
        print("List has been sorted")
        break
    print()
    print("*********************************")
print("While loop iterations needed: " + str(turn))


