import os
os.system("cls")
def draw_table(T):
    for item in T:
        print(item)
    print("\n")

def dist(X, Y):
    (m, n) = (len(X), len(Y))

    T = [[0 for x in range(n + 1)] for y in range(m + 1)]

    for i in range(1, m + 1):
        T[i][0] = i                    # (case 1)

    for j in range(1, n + 1):
        T[0][j] = j                    # (case 1)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # _ = input()
            os.system("cls")
            print("\n{} - {}".format(i, j))
            print('"{}" - "{}"'.format(X[:i], Y[:j]))
            if X[i - 1] == Y[j - 1]:            # (case 2)
                if i > 1 and j > 0:
                    print('==> "{}" - "{}" = {}'.format(X[:i-1], Y[:j-1], T[i-1][j-1]))
                T[i][j] = T[i-1][j-1]
            else:
                print("insert = ", T[i][j-1] + 1)
                print("delete = ", T[i-1][j] + 1)
                print("update = ", T[i-1][j-1] + 1)
                T[i][j] = 1 + min(
                                    T[i][j-1],
                                    T[i-1][j],
                                    T[i-1][j-1]
                                )
            
            draw_table(T)

    return T[m][n]


if __name__ == '__main__':
    

    X = "cocacola"
    Y = "colacoca"

    print("The Levenshtein distance is", dist(X, Y))