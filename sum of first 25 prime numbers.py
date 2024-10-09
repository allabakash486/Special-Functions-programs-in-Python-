def prime(num):
    if num>2:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True
    return False
var= list(filter(prime,range(1,int(input('Enter the number range:')))))
Sum_of_val = 0
for i in var:
    Sum_of_val +=i
print(Sum_of_val)