def Happy(number):
    while (9< number):
        sol = 0
        while number!=0:
            sol += (number%10)**2
            number //= 10
        number = sol
    return number==1 or number ==7
print(list(filter(Happy,range(1,int(input('Enter the range:'))+1))))
