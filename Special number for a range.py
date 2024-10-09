def Special(number):
    Dup= number
    sol = 0
    while number!=0:
        fa = 1
        ld = number%10
        for i in range(1,ld+1):
            fa *= i
        sol += fa
        number //= 10
    return Dup==sol
print(list(filter(Special,range(1,int(input('Enter the range:'))+1))))