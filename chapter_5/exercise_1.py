def count_numbers():
    total = 0
    count = 0

    while True:
        user_input = input('Enter integer or done: ')
        if user_input == 'done':
            break
        try:
            total += int(user_input)
            count += 1
        except:
            print('Invalid input')
            continue
    
    average = total / count
    print(total, count, average)

if __name__ == '__main__':
    count_numbers()
