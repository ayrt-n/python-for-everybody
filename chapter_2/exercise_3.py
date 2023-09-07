def calculate_gross_pay():
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
    print(f'Pay: {hours * rate}')

if __name__ == '__main__':
    calculate_gross_pay()
