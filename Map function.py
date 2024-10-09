# By using map function we can print square of the numbers
def square(num):
    return num**2
print(list(map(square , range(1,21))))