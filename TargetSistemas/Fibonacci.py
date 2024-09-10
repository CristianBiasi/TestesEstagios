print("Sequência de Fibonacci")
first = int(input("Digite o primeiro número: "))
last = int(input("Digite o último número que queira saber: "))

prev = 0
next = 1

print("Sequência Fibonacci:")
print(prev)

while next <= last:
    print(next)
    temp = prev + next
    prev = next
    next = temp
m