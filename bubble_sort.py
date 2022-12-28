
given_array = [3, 1, 5, 7, 2, 4, 4, 4, 9, 8, 7]
sorted_array = []

length_array = len(given_array)
n = length_array
turn = 0

while (n>1):
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
    n = n - 1
    if swapped == False:
        print("List has been sorted")
        break
    print()
    print("*********************************")
print("While loop iterations needed: " + str(turn))


