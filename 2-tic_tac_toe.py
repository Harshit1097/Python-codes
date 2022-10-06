def board(mat):
    print(3 * ' ---')
    print(f'| {mat[0][0]} | {mat[0][1]} | {mat[0][2]} |')
    print(3 * ' ---')
    print(f'| {mat[1][0]} | {mat[1][1]} | {mat[1][2]} |')
    print(3 * ' ---')
    print(f'| {mat[2][0]} | {mat[2][1]} | {mat[2][2]} |')
    print(3 * ' ---')


def checker(z):
    for i in range(3):
        aset = set(z[i])
        if len(aset) == 1 and z[i][0] != " ":
            return z[i][0]

    for j in range(3):
        bset = {z[0][j], z[1][j], z[2][j]}
        if len(bset) == 1 and z[0][j] != " ":
            return z[0][j]

    diag1 = {z[0][0], z[1][1], z[2][2]}
    diag2 = {z[0][2], z[1][1], z[2][0]}
    if len(diag1) == 1 or len(diag2) == 1 and z[1][1] != " ":
        return z[1][1]


a = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

counter = 0

while True:
    c = [int(x)-1 for x in input("Player 1 : Enter coordinates where you wanna put x : ").split(",")]
    if a[c[0]][c[1]] == ' ':
        a[c[0]][c[1]] = 'x'
    else:
        c = [int(x)-1 for x in input("Occupied! Enter again for x : ").split(",")]
        a[c[0]][c[1]] = 'x'
    board(a)

    result = checker(a)
    if result == 'x':
        print('Player 1 won !!')
        break

    if counter == 4:
        print('Game draw !!')
        break

    d = [int(x)-1 for x in input("Player 2 : Enter coordinates where you wanna put o : ").split(",")]
    if a[d[0]][d[1]] == ' ':
        a[d[0]][d[1]] = 'o'
    else:
        d = [int(x) - 1 for x in input("Occupied! Enter again for o : ").split(",")]
        a[d[0]][d[1]] = 'o'
    board(a)

    counter += 1

    result = checker(a)
    if result == 'o':
        print('Player 2 won !!')
        break
