a = int(input())
b = int(input())
print(a + b)
print(a - b)
print(a * b)
n = int(input().strip())

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")

    
a = int(input())
b = int(input())


int_division = a // b
float_division = a / b


print(int_division)
print(float_division)

n = int(input())
for i in range(n):
    print(i * i)

if __name__ == "__main__":
    n = int(input().strip())
    for i in range(1, n+1):
        print(i, end="")