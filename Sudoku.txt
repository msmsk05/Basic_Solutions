satır = ""
row = 3
for i in sudoku:
    for j, k in enumerate(i):
        if row == 3:
            print(11 * "- ")
            row = 0
        satır += str(k) if j % 3 or j == 0 else "|" + str(k)
    row += 1
    print(*satır)
    satır = ""
print(11 * "- ")