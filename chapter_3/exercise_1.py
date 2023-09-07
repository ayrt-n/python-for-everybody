def calculate_gross_pay():
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))

    # Increase overtime hours by 1.5
    if hours > 40:
        hours = 40 + (hours % 40) * 1.5

    print(f'Pay: {hours * rate}')

if __name__ == '__main__':
    calculate_gross_pay()
