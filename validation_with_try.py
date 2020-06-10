NUMBER_TESTS = 3
def average():
    #Get input for scores
    average_scores = (score1 + score2 + score3) / 3
    print('average: ', (score1 + score2 + score3) / 3)
    # declare variables. use score1, score2, score3 in calculation
    return average_scores

def average(score1, score2, score3):
    NUMBER_TESTS = 3
    return float((score1 + score2 + score3)/NUMBER_TESTS)



if __name__ == '__main__':
    score1 = int(input('score 1: '))
    score2 = int(input('score 2: '))
    score3 = int(input('score 3: '))
    #Calculate average scores
    average_scores = average(score1, score2, score3)
    print(average_scores)

    if score1 < 0:
        raise ValueError('score1 should not be less than 0!')
