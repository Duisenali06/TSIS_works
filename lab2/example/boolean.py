print(10 > 9)
print(10 == 9)
print(10 < 9)

#true
#false
#false


a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
#b is greater than a 

print(bool("Hello"))
print(bool(15))

#true
#true

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#true
#true

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
#true
#true
#true

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#all False


def myFunction() :
  return True

print(myFunction())

#True

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
  
#YES!

x = 200
print(isinstance(x, int))

#True