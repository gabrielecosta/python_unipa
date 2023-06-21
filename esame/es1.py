def fun8(matricola):
    x = [int(i) for i in matricola]
    y = [int(matricola[i]) for i in range(len(matricola)-1,-1,-1)]
    count = 0
    print(x)
    print(y)
    for idx in range(len(x)):
        if x[idx]==y[idx]:
            count +=1
    return (count+2)%4


print(fun8('0711990'))