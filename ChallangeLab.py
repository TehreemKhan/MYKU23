l=list()
for num in range(1,250):
    for x in range(2,num):
        if(num % x ) ==0:
            break
    else:
        l.append(num)

with open("results.txt","w")as f:
    f.write(str(l))
