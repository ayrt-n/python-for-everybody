def calculate_gross_pay():
    try:
        hours = float(input('Enter Hours: '))
        rate = float(input('Enter Rate: '))

        # Increase overtime hours by 1.5
        if hours > 40:
            hours = 40 + (hours % 40) * 1.5

        print(f'Pay: {hours * rate}')
    except:
        print('Error, please enter numeric input')

if __name__ == '__main__':
    calculate_gross_pay()
