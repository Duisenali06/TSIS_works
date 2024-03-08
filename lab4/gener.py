#ex1
def square_generator(N):
    n = 0
    while n <= N:
        yield n ** 2
        n += 1
N = int(input())
for square in square_generator(N):
    print(square)


#ex2
n = int(input())

for i in range(0, n+1, 2):
  if i < n - 1:
    print(i, end = ',' )
  else:
    print(i)

#ex3
def generate_divisible_by_3_and_4(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 4 == 0:
            print(i)
            
generate_divisible_by_3_and_4(n)

#ex4
def generate_squares_a_b(a, b): 
    for i in range(a, b):
        print(i**2)
generate_squares_a_b(n, n)

#ex5
def down(n):
    while n >= 0:
        yield n
        n -= 1


n = int(input())
for num in down(n):
    print(num)
