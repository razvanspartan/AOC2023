f=open("input.txt", "r")
sum=0
for line in f:
    for i in range(0,len(line)):
        if(line[i].isnumeric()):
            c1=line[i]
            break
    print(c1)
    for i in range(len(line)-1,-1,-1):
        if(line[i].isnumeric()):
            c2=line[i]
            break
    print(c2)
    sum=sum+int(c1+c2)
print(sum)
