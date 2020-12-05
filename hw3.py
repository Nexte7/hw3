def guas_seidel(mat, b, x):
    mat_size = len(mat)
    xr_ans = x.copy()
    for j in range(mat_size):
        d = b[j]
        sum = 0
        for i in range(mat_size):
            sum += mat[i][j]
            if i != j:
                d -= mat[j][i] * xr_ans[i]
        sum -= mat[i][i]
        xr_ans[j] = (d / mat[j][j])

    if sum > mat[i][i]:
        flag_diag = False
        #print("There is no dom diagonal.")
    else:
        flag_diag = True
        #print("There is a dom diagonal.")
    return [xr_ans,flag_diag]


def jacobi(mat, b, xr):
    mat_size = len(mat)
    xr = xr.copy()
    xr_ans = []
    for j in range(mat_size):
        d = b[j]
        sum = 0
        for i in range(mat_size):
            sum += mat[i][j]
            if i != j:
                d -= mat[j][i] * xr[i]
        sum -= mat[i][i]
        xr_ans.append(d / mat[j][j])

    if sum > mat[i][i]:
        flag_diag = False
        # print("There is no dom diagonal.")
    else:
        flag_diag = True
        # print("There is a dom diagonal.")
    return [xr_ans,flag_diag]


def check_epsilon(epsilon, x, xr_1):
    flag = True
    solution = x.copy()  # [item for item in x]
    next_solution = xr_1.copy()  # [item for item in xr_1]
    for i in range(len(solution)):
        if epsilon > abs(next_solution[i] - solution[i]):
            flag = False
    return flag


def main():
    mat = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
    b = [2, 6, 5]
    xr = [0, 0, 0]

    print("\n\nJacobi:\n")
    condition = True
    epsilon = 0.001
    count = 0
    while condition:
        xr_1, flag_diag = jacobi(mat, b, xr)
        x_formatted = list(map(lambda y: "{:.6f}".format(y), xr_1))
        print(f"{count + 1}\t{x_formatted}")
        condition = check_epsilon(epsilon, xr, xr_1)
        xr = xr_1
        count += 1
    if flag_diag:
        print("There is a dom diagonal.")
    else:
        print("There is no dom diagonal.")


    print("\n\nGauss Seidel:\n")
    condition = True
    count = 0
    xr = [0, 0, 0]
    while condition:
        xr_1, flag_diag = guas_seidel(mat, b, xr)
        x_formatted = list(map(lambda y: "{:.6f}".format(y), xr_1))
        print(f"{count + 1}\t{x_formatted}")
        condition = check_epsilon(epsilon, xr, xr_1)
        xr = xr_1
        count += 1
    if flag_diag:
        print("There is a dom diagonal.")
    else:
        print("There is not dom diagonal.")

main()
