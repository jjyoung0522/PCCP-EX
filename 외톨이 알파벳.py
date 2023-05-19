def solution(input_string):
    count = {}
    for a in input_string:
        if a in count:
            count[a] += 1
        else:
            count[a] = 1

    alpha = []

    for a, number in count.items():
        if number >= 2:
            substring = a * number
            if substring not in input_string:
                alpha.append(a)

    if not alpha:
        answer = 'N'
    else:
        answer = ''.join(sorted(alpha))
    return answer
