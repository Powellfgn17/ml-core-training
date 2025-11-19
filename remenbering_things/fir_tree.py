rows =10
for i in range(1,rows + 1):
    print(" " * (rows - i) + " *" * i)

columns = rows -1
for j in range(1, 4):
    print(' ' * columns +"| |")

print("__" * rows)