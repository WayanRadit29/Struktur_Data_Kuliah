stack = []
N = int(input())

for _ in range(N):
    a = input()
    a = list(a)
    if a[0] == '+':
        stack.append(int(a[1]))
        print(len(stack))
    elif a[0] == '-':
        b = stack.pop()
        print(f"{b} : {stack}")

