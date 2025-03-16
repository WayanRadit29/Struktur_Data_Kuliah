from collections import deque

N = int(input())
for _ in range(N):
    long_text = input()
    home_res = deque()
    end_res = deque()
    current_text = ""
    mode = "end"
    
    for char in long_text:
        if char == '[':
            if mode == "end":
                end_res.append(current_text)
            else:
                home_res.appendleft(current_text)
            current_text = ""
            mode = "home"
        elif char == ']':
            if mode == "home":
                home_res.appendleft(current_text)
            else:
                end_res.append(current_text)
            current_text = ""
            mode = "end"
        else:
            current_text += char

    if mode == "home":
        home_res.appendleft(current_text)
    else:
        end_res.append(current_text)

    
    print("".join(home_res) + "".join(end_res))







