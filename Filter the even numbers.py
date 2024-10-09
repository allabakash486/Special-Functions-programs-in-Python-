def even(number):
    if number%2==0:
        return True
    return False
print(list(filter(even,range(1,101))))