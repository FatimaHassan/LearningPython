# program to create List from comma separated values
def createTuples():
  emptyTuple = ()
  values = input("Input some comma seprated numbers : ")
  list = values.split(",")
  print('List : ',list)
  print('1st item is',list[0])
  print(tuple(list))
  emptyTuple = tuple(list)
  print(emptyTuple)
  print(emptyTuple)

createTuples()

