S = []
S.append(0)

T = int(input())
for i in range(T):
    Q = int(input())
    for query in range(Q):
        sec = int(input())
        X = int(input())
        if sec == 0:
            S.append(X)
        elif sec == 1:
            S[S.index(X)] = X^4

        for val in S:
            print(S)