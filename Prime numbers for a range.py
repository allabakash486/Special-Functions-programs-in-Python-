def prime(number):
    if number>2:
        for i in range(2,int(number**0.5)+1):
            if number %i == 0:
                return 'Not'
        return 'prime number'
    return 'Not'
print(list(map(prime,range(1,int(input('Enter the range:'))+1))))