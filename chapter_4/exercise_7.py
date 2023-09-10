def compute_grade(score):
    if score < 0 or score > 1:
        print('Error, score must be between 0.0 and 1.0')
    elif score < 0.6:
        print('F')
    elif score < 0.7:
        print('D')
    elif score < 0.8:
        print('C')
    elif score < 0.9:
        print('B')
    else:
        print('A')

if __name__ == '__main__':
    compute_grade(0.8)
