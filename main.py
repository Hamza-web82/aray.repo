name = input("Enter your password:\fpassword\r\t\t    ")

name = input("Enter your password:\npassword\r")

x = 1
y = 2
sum = x + y

x = [1,2,3,4]

print(x[3])

a = "Hello, World!"
print(a[1])

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


name = input("enter your name: ")
print("welcome ", name)


str = "apple"
print(str[2:4])

str = "the best things in life are free"
print(str.replace("e","a"))

for x in "banana":
  print(x)


a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best \"things\" in life are free!"
print("expensive" not in txt)

b = "Hello, World!"
print(b[:5])

a = "Hello"
b = "world"
c = a + " " + b
print(c)

age = 20 
txt = f"My name is hamza, i am {age}"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

cars = ["Ford", "Volvo", "BMW"]
cars[2] = "grande"
print(cars)

txt = (1,2,3,4,5,6,7,8)
for x in txt:
    print(x)

a = 1
while a < 25:
    print(a)
    a += 1

a = 1
while a < 9:
    print(a)
    if(a == 5):
        break
    a += 1

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

txt = "1\t2\t3\n4\t5\t6\n7\t8\t9"
print (txt)

txt = "\t2\t\n3\t4\t5\n\t6"
print(txt)

x = (2 * 12 == 24)
y = (3 * 13 == 36)
z = x
print(x is z)
print(x is y)
print(x == y)


result = ((2 * 12) / (3 * 12)) == (24/36)
print(result)


txt = ((4 * 15) / (3 * 20)) ==(60 / 60)
print(txt)

if (0.1 + 0.2 == 0.3):
    print('True')
else:
    print('False')

list1 = ["abc", 34, True, 40, "male"]
print(list1)

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"

print(thislist)


thislist = ["apple", "banana", "cherry"]

thislist.append("orange")

print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


thislist = ["apple", "banana", "cherry"]
txt = ["mango", "pineapple", "papaya"]

thislist.extend(txt)

print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "n" in x:
        newlist.append(x)

print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if x != "apple"]

print(newlist)


newlist = [x for x in range(10)]

print(newlist)

