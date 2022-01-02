def solution(P, T, A, B):
    # write your code in Python 3.6
    N = len(P) #number of participant

    connectedp = [[] for _ in range(N)] #define conectted components
    for a, b in zip(A, B):
        connectedp[a].append(b)
        connectedp[b].append(a)
    visit = [False] * N

    for i in range(N):
        if not visit[i]:
            visit[i] = True
            q = [i] #list of partisipants that are in the same connected component
            sumvalue = 0
            while q:
                v = q.pop() #take any P from list and removed from list
                sumvalue += P[v] - T[v]
                for a in connectedp[v]:
                    if not visit[a]: #if P not visited before
                        visit[a] = True
                        q.append(a)   #put in a list

            if sumvalue != 0:
                return False
    return True
