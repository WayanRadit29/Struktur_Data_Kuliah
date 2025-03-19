import sys
from collections import deque

result = []
input_data = sys.stdin.read().splitlines()  # Membaca semua input sekaligus, lalu split ke baris

for processed_text in input_data:
    home_res = deque()
    end_res = deque()
    current_text = ""
    mode = "end"

    for char in processed_text:
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

    result.append("".join(home_res) + "".join(end_res))

sys.stdout.write("\n".join(result) + "\n")  # Cetak sekaligus untuk menghindari overhead print()
