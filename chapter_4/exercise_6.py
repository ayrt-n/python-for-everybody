def compute_pay(hours, rate):
        if hours > 40:
            hours = 40 + (hours % 40) * 1.5

        print(f'Pay: {hours * rate}')

if __name__ == '__main__':
    compute_pay(50, 16)
