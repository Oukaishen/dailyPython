
seasons = ['Spring','Summer','Fall','Winter']
print(list(enumerate(seasons)))
print(list(enumerate(seasons,start=2)))

for index, element in enumerate(seasons):
    print("Now the index is {} and the element is {}".format(index,element))