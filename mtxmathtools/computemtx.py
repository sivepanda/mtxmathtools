from sympy import *

avail_operations = {
    "1" : "Reduced Row Echelon Form",
    "2" : "Null Space",              
    "3" : "Column Space",              
    "4" : "Transpose",              
    "5" : "Left Null Space",              
    "6" : "Transpose Row Echelon Form",              
    "7" : "Determinant",              
    "8" : "Eigenvectors",              
    "9" : "Diagnonalize",              
    "10" : "Normalize Columns",             
    "11" : "Multiply with Another Matrix",              
    "12" : "Multiply with Transpose (AAT)",              
    "13" : "Multiply with Transpose (ATA)",              
    "14" : "Singular Value Decomposition",              
    "15" : "Gram-Schmidt (Columns are Vectors)"
}

def inputMatrix():
    print("Input the matrix line by line. Press enter when you are done.\n")
    matrix = []
    line = ""
    while (line != "done"):
        line = input()
        if(not line.strip()):
            break
        from fractions import Fraction
        line = line.strip().split()
        line = [sympify(entry.replace("i", "I")) for entry in line]
        matrix.append(line)

    return Matrix(matrix)

def main():
    correctMatrix = "no"

    while correctMatrix == "no":
        a = inputMatrix()
        print("Is this the matrix you wanted?")
        pprint(a)
        correctMatrix = input("Type 'yes' if this is the correct matrix, otherwise, type 'no'\n")

    # Pre-calculate Transpose for later use
    a_t = a.T

    # Create an identity matrix of matching column size.
    idenn = eye ( shape(a)[0] )

    print("\n\nSelect the operation you would like to compute. Type the number of your choice.\nIf you would like to compute multiple things, enter both numbers delineated by a space.\n")
    op = input("".join(f"{key}\t{val}\n" for key, val in avail_operations.items()))
    print("\n")

    for operation in op.split(" "):
        out = "Invalid Operation."
        print(avail_operations[operation] + "========")
        if (operation == "1"):
            out = a.rref(pivots=False)
        if (operation == "2"):
            out = a.nullspace()
        if (operation == "3"):
            out = a.columnspace()
        if (operation == "4"):
            out = a_t
        if (operation == "5"):
            out = a_t.nullspace()
        if (operation == "6"):
            out = a_t.rref(pivots=False)
        if (operation == "7"):
            out = a.det()
        if (operation == "8"):
            eig =input("If you would like to calculate the eigenvectors for a particular value, enter it. If not, hit enter.\n")
            print("\n")
            if(len(eig) == 0):
                out = a.eigenvects()
            else:
                eig = sympify(eig)
                out = ( a - ( eig * idenn ) ).nullspace()
        if (operation == "9"):
            c, d = a.diagonalize()
            print("C===")
            pprint(c)
            print("D===")
            out = d
        if (operation == "10"):
            outcols = []
            cols = [a.col(i) for i in range(a.cols)]
            for col in cols:
                outcols.append( col / col.norm() )
            out = Matrix.hstack(*outcols)

        if (operation == "11"):
            correctMatrix = "no"
            while correctMatrix == "no":
                b = inputMatrix()
                print("Is this the matrix you wanted?")
                pprint(b)
                correctMatrix = input("Type 'yes' if this is the correct matrix, otherwise, type 'no'\n")
                print("Result===")
                out = a * b

        if (operation == "12"):
            out = a * a_t

        if (operation == "13"):
            out = a_t * a

        if (operation == "14"):
            out = a.singular_value_decomposition() 

        if (operation == "15"):
            print("WARNING: Takes a naive approach, uses first col as u1, regardless of ease of calculation")
            outcols = []
            cols = [a.col(i) for i in range(a.cols)]
            outcols.append(cols.pop(0))
            for col in cols:
                curr = col
                for c in outcols:
                    curr = curr - ( c.dot(col) / c.dot(c)) * c
                outcols.append(curr)
            out = Matrix.hstack(*outcols)

        pprint(out)
        print("\n")

    again = input("Would you like to perform another computation? Enter 'yes' or 'no'\n")
    if again == "yes":
        main()


if __name__ == "__main__":
    main()
