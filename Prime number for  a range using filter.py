def prime(num):
    if num>2:
        for i in range(2,int(num **0.5)+1):
            if num%i==0:
                return False
        return True
    return False
print(list(filter(prime,range(1,101))))