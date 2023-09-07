def score_to_grade():
    try:
        score = float(input('Enter Score (0.0 to 1.0): '))

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
    except:
        print('Error, please enter numeric input')

if __name__ == '__main__':
    score_to_grade()
