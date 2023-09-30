from googlesearch import search
query = input("Enter Your Search: ")

for i in search(query, 10, advanced= True):
    print(i.title)
    print(i.url)
    print(i.description)
    print()
