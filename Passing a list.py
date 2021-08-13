user_list = [2,3,4,5,6,7,79,7,5,4,9]


def count(user_lst):
    even = 0
    odd = 0
    for number in user_lst:
        if number % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd


even, odd = count(user_list)

print('Total Odd Number: ',odd)
print('Total Even Number: ',even)