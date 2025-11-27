#learning python
print('hello world')

first_name = 'John'
print(len(first_name))

is_student = False

if is_student:
    print('you are a student')
else: 
    print('you are not a student') 



thisiList = ['zohn', 'jane', 'moe', 'aim']
thatlist= list(('jack', 'jones', 'james'))
thistuples = tuple(('jill', 'jill', 'jill'))
thisiList.append('jill')
thisiList.sort()
newLists = thisiList.copy()
print(newLists)
# this is used to map through object or array
for x in thisiList:
    print(x)

newList = []

for x in thatlist:
    if "a" in x: 
        newList.append(x)
        print(newList)

# to write a comprehension the syntax includes 
# [expression for item in iterable if condition == True]
newList = [x for x in thatlist if "a" in x]

#to craete a class use the class keyword
class newClass:
    def myfunc(self, name):
        print('hello ' + name)
    classList = ['john', 'jane', 'moe', 'aim']
    for x in classList:
        print(x)
    def __init__(self):
        classList = ['john', 'jane', 'moe', 'aim']
        for x in classList:
            print(x)

# to create an object of a class
p1 = newClass()
p1.myfunc('jagun')
p2 = newClass()

animals = ['animal', 'place',  'things']
#iterate over it using the for loop
for x in animals:
    print(x)
#loop through based off a particular text
for x in animals:
    if x == 'place':
        break
    print(x)

mystr = 'banana'
myit = iter(mystr)
print(next(myit))

import requests
url = 'https://jsonplaceholder.typicode.com/posts/1'

try: 
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print('error fetching data:', e)
else: 
    print('data fetched successfully')
    print(response.json())
