def Reverse(number):
    sol = 0
    while number!=0:
        sol = sol*10 +(number%10)
        number //= 10
    return sol
print(list(map(Reverse,range(1,int(input('Enter the range:'))+1))))
