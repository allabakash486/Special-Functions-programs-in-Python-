# This program will print the only prime numbers which are present in the given range
def prime(num):
    if num>1:
        for ind in range(2,int(num**0.5)+1):
            if num%ind==0:
                return False
        return True
    return False
print(list(filter(prime,range(1,101))))