from sympy import *

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
    op = input("1\tReduced Row Echelon Form\n2\tNull Space\n3\tColumn Space\n4\tTranspose\n5\tLeft Null Space\n6\tTranspose Row Echelon Form\n7\tDeterminant\n8\tEigenvectors\n9\tDiagnonalize\n")
    print("\n")

    for operation in op.split(" "):
        out = "Invalid Operation."
        if (operation == "1"):
            print("Reduced Row Echelon Form====")
            out = a.rref(pivots=False)
        if (operation == "2"):
            print("Null Space====")
            out = a.nullspace()
        if (operation == "3"):
            print("Column Space====")
            out = a.columnspace()
        if (operation == "4"):
            print("Transpose====")
            out = a_t
        if (operation == "5"):
            print("Left Null Space====")
            out = a_t.nullspace()
        if (operation == "6"):
            print("Transpose Row Echelon Form====")
            out = a_t.rref(pivots=False)
        if (operation == "7"):
            print("Determinant====")
            out = a.det()
        if (operation == "8"):
            print("Eigenvectors====")
            eig =input("If you would like to calculate the eigenvectors for a particular value, enter it. If not, hit enter.\n")
            print("\n")
            if(len(eig) == 0):
                out = a.eigenvects()
            else:
                eig = float(eig)
                out = ( a - ( eig * idenn ) ).nullspace()
        if (operation == "9"):
            print("Diagonalize====")
            c, d = a.diagonalize()
            print("C===")
            pprint(c)
            print("D===")
            out = d


        pprint(out)
        print("\n")

    again = input("Would you like to perform another computation? Enter 'yes' or 'no'\n")
    if again == "yes":
        main()


if __name__ == "__main__":
    main()
