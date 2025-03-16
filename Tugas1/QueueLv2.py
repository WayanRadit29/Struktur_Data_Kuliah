queue = []
N = int(input())
done = False

for _ in range(N):
    a = input()
    a = list(a)
    if a[0] == '+':
        queue.append(int(a[1]))
    elif a[0] == '-':
        if not queue:
            done = True
            print(f"Antrian sudah kosong : {queue}")
            break
        else: 
            queue.pop(0)

if not done:
    print(queue)