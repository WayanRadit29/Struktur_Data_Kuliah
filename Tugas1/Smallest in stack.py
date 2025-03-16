N = int(input())

main_stack = []
min_stack = []

for _ in range(N):
    masuk = input().split(" ")
    masuk = list(masuk)

    if masuk[0] == "PUSH":
        main_stack.append(int(masuk[1]))

        if not min_stack:
            min_stack.append(int(masuk[1]))
            
        else:
            if min_stack[-1] > int(masuk[1]):
                min_stack.append(int(masuk[1]))

    elif masuk[0] == "MIN":
        if min_stack:
            print(min_stack[-1])
    
    elif masuk[0] == "POP":
        a = main_stack.pop()

        if a == min_stack[-1]:
            min_stack.pop()





        

            


    




    

