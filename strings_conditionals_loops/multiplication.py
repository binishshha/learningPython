for i in range(1,11):
    for j in range(1,11):
        print(f'{i}*{j}={i*j}')

for i in range(1,11):
    row=""
    for j in range(1,11):
        row+=str(i*j)+"\t"
    print(row)

i=1
while i<11:
    j=1
    roww=""
    while j<11:
        roww+= str(i*j)+"\t"
        j+=1
    print (roww)
    i+=1       