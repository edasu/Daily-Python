def solution(inputString):
    letters = list(inputString)    
    solution = True
    i = 0

    while len(letters) > 0 and solution:       
        if letters[0] != letters[(len(letters) - 1)]:
            solution = False
        else:
            letters.pop(0)
            if len(letters) > 0:
                letters.pop((len(letters) - 1))

    return solution