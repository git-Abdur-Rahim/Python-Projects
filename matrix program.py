def matrix_mul(c, d, A, f, h,
               B):  
    if d != f:  # For defining function and usage of if else statements I referred stackoverflow
        print("Matrix Multiplication is NOT POSSIBLE")
        print("Matrix order must be same since, \nThe matrix A column is " + str(+d) + "\nThe matrix B row is " + str(
            +f) + "\nRe enter order")
        matrix_AB()

    else:
        AB = []
        # To create a 0-matrix AB of order m x q I referred Java2Blog
        for i in range(c):
            row = []
            for j in range(h):
                row.append(0)
            AB.append(row)
        print("Matrix Multiplication Of A*B : ")
        # To perform matrix multiplication I referred Java2Blog using nested for loops
        for i in range(c):
            for j in range(h):
                for k in range(d):
                    AB[i][j] += A[i][k] * B[k][j]
        # For printing multiplied matrix printing row wise I referred Java2Blog
        for row in AB:
            print(row)


# The input process from the user is to run the for loop so that my code doesn't terminates itself if we give wrong matrix order it runs again and again until it successfully completes the multiplication
procces = (int(input("Enter No. of times to perform Matrix Mulplication : ")))
for i in range(procces):
    def matrix_AB(): 
     
        print("Enter order of 1st matrix:")  # For getting input from user for both matrix A and B I referred Java2Blog
        #  To take integer inputs in one line I referred Java2Blog
        c, d = list(
            map(int, input().split())) 
        print("Enter Row wise values")
        A = []
        # For row wise insertion in the matrix I referred Java2Blog
        for i in range(c):
            print("Enter row", i, "value:")
            # To take 1d- integer array input in one line I referred Java2Blog
            row = list(
                map(int, input().split()))  
            A.append(row)

        print("Enter order of 2nd matrix:")
        # To take integer inputs in one line I referred Java2Blog
        f, h = list(
            map(int, input().split()))  
        print("Enter Row wise values")
        B = []
        # For row wise insertion in the matrix I referred Java2Blog
        for j in range(f):
            print("Enter row", j, "value:")
            # To take 1d- integer array input in one line I referred Java2Blog
            row = list(
                map(int, input().split())) 
            B.append(row)

        print("Matrix A: ")  # for printing matrix in row wise Matrix A and B I referred
        for row in A:
            print(row)

        print("Matrix B: ")
        for row in B:
            print(row)
        matrix_mul(c, d, A, f, h,
                   B)  

    matrix_AB()  # for calling matrix_mul and matrix_AB I referred stackoverflow
