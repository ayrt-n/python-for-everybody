def minmax_numbers():
    min = None
    max = None

    while True:
        user_input = input('Enter integer or done: ')
        if user_input == 'done':
            break
        try:
            number = int(user_input)
            if min == None or number < min:
                min = number
            if max == None or number > max:
                max = number
        except:
            print('Invalid input')
            continue
    
    print(min, max)

if __name__ == '__main__':
    minmax_numbers()
