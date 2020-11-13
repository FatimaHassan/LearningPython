#Write a function named whichtakes a single parameter, which is a string.
#Should return a list of all the indexes in the string that have capital letters.

def capital_indexes():
    str1=input("Enter String with capital and small letters")
    list1=[]
    list2 = []
    list1[:0] = str1
    for i in list1:
        if i.isupper() == True:
            list2.append(list1.index(i))
    print(list2)

capital_indexes()
