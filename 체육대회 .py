from itertools import permutations

def solution(ability):
    n = len(ability)  
    m = len(ability[0])
    
    max_total = 0

    students = list(range(n))
    perm = permutations(students, m)

    for p in perm:
        total = 0 
        selected = [False] * n

        for i in p:
            if not selected[i]:
                selected[i] = True
                total += ability[i][p.index(i)]

        max_total = max(max_total, total)

    return max_total
