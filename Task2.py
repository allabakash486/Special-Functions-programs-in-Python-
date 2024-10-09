li = []
def adding_elements_in_list(li):
    length = int(input('Enter the length of list:'))
    for ind in range(length):
        i = int(input('Enter the elemnts:'))
        li.append(i)
    print(li)
adding_elements_in_list(li)
