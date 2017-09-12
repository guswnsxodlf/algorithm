# Created by Jello on 2017. 9. 13.

while True:
    lines = int(input())
    text = []

    if lines == 0:
        break

    for i in range(lines):
        text.append(input())

    col = 0
    row = 0
    while len(text) > row:
        if len(text[row]) <= col or text[row][col] == ' ':
            row += 1
        else:
            col += 1

    print(col+1)
