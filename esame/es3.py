def fun3(matricola):
    if int(matricola)%2 == 0:
        result = 0
        for x in matricola:
            if int(x)>result:
                result = int(x)
    else:
        result = 9
        for x in matricola:
            if int(x) < result:
                result = int(x)
    return result%4

def fun1(matricola):
    x = [i for i in matricola[0:-2]]
    y = x[-3]
    z = int(y) % 4
    return z

def fun4(matricola):
    num = int(matricola[1:3])
    n = 0
    while num > 0:
        a = num%10
        num = num-a
        num = num // 10
        n = n*10 + a

    return n%4

#print(fun3('0711990'))
print(fun4('0711990'))