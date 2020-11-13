#Write a function that takes a string return the middle letter.
#If there is no middle letter, your function should return the empty string.

def mid():
    str1 = input("Enter String:")
    list1 = []
    list1[:0] = str1
    check = int(len(list1) % 2)
    if check == 0:
        print ("''")
    else:
        midValue = int((len(list1) / 2))
        print(list1[midValue])

mid()




