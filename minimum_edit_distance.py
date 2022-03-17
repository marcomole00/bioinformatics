#first = input("first sequence: ")
#second = input("second sequence: ")
first = "saturday"
second = "sunday"

a = len(first)+1
b = len(second)+1

table = [0] * a




for x in range(a):
    table[x] = [0]*b

for i in range(a):
    for j in range(b):
        if i == 0:
           table[i][j] = j
        elif j == 0:
           table[i][j] = i
        else:
            if first[i-1] == second[j-1]:
                table[i][j] = min(1+table[i][j-1], 1+table[i-1][j], table[i-1][j-1] )
            else:
                table[i][j] = min(1+table[i][j-1], 1+table[i-1][j], 1+ table[i-1][j-1] )


for line in table:print(line)




