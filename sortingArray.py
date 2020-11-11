def sortArray():
    values = []
    number = int(input("Enter number of elements in an array"))
    for i in range (number):
        values.append(int(input("Enter Number")))


    for i in range (0, number):
        for j in range (i+1,number):
            if values[i] > values[j]:
                temp = values[i]
                values[i] = values[j]
                values[j] = temp

    print(values)


sortArray()