first = input("first sequence: ")
second = input("second sequence: ")
from functools import partial


first = "sugar"
second = "sucre"

a = len(first)+1
b = len(second)+1

table = [0] * a

for x in range(a):
    table[x] = [0]*b


alignments = list()

def backtrack (i,j, partial_1, partial_2):
    if i +j == 0:
        
        alignments.append((partial_1[::-1],partial_2[::-1])) #todo in reverse
        return
    else:
        min_value = min(table[i-1][j], table[i][j-1], table[i-1][j-1])
        if table[i][j-1] == min_value: #left path
            backtrack(i,j-1,partial_1+"-", partial_2+second[j-1])
        if table[i-1][j] == min_value: #up path
            backtrack(i-1,j,partial_1+first[i-1], partial_2+"-")
        if table[i-1][j-1] == min_value: #diagonal path
            backtrack(i-1,j-1,partial_1+first[i-1], partial_2+second[j-1])
        



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


for line in table: print(line)

backtrack(a-1,b-1,"","")

for align in alignments:
    print(align[0])
    print(align[1])
    print()

