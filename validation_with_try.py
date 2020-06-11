NUMBER_TESTS = 3
def average():
    #Get input for scores
    # declare variables. use score1, score2, score3 in calculation
    return average_scores

def average(score1, score2, score3):
    NUMBER_TESTS = 3
    if 0<score1<=100:
        print("score1 is within range.")
    if 0<score2<=100:
        print("score2 is within range.")
    else:
        print("score must be positive.")
        raise ValueError
    return float((score1 + score2 + score3)/NUMBER_TESTS)

score1 = int(input('score 1: '))
score2 = int(input('score 2: '))
score3 = int(input('score 3: '))
#Calculate average scores
average_scores = average(score1, score2, score3)
print(average_scores)

if __name__ == '__main__':
    pass
