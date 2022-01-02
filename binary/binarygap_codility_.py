def solution(N):
    # bin(). This function takes an input of type Integer
    # and returns a binary string prefixed with 0b
    # Assign result to variable 'br' (Binary  Represenation)
    # Use [2:] to remove first 2 chars from returned string
     br = str(bin(N))[2:]
     #create the groups of zeros that fall between a 1 and  1
     br_group = False
     br_highest = 0
     bin_zero_counter = 0
    #This for loop will assign each iteration character to that loop instance of char
     for char in br:
             if br_highest < bin_zero_counter:
                 br_highest = bin_zero_counter
            #start the group tracker
             br_group = True
             bin_zero_counter = 0
         elif br_group:
             bin_zero_counter += 1
     return br_highest

N = 1041
print(solution(N))
