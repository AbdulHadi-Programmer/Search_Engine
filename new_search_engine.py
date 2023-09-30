from googlesearch import search

data = input("Enter Your Search: ")
#print(search(data)) 

for i in search(data):
    print(i)
