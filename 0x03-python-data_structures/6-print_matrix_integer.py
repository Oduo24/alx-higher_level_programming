#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for elm in matrix:
            string_v = [str(i) for i in elm]
            res = " ".join(string_v)
            print("{}$".format(res))
        print("--$")
        print("$")
