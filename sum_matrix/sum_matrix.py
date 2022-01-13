def solution(matrix):
    count_room= 0
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if matrix[j][i] == 0:
                #print("Hunted room stay away")
                break
            else:
                count_room += matrix[j][i]
    return count_room