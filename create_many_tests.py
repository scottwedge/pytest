#!/usr/bin/env python3

# Script to create multiple functions and pytests for them

def create_def(n):
    f.write("def num{}(x):".format(n))
    f.write("\n")
    f.write("    return x")
    f.write("\n")
    f.write("")
    f.write("\n")

def create_test_def(n):
    f.write("def test_num{}():".format(n))
    f.write("\n")
    f.write("    assert num{}({}) == {}".format(n, n, n))
    f.write("\n")
    f.write("")
    f.write("\n")

file = "tests.py"
max = 10

with open(file, "w") as f:
    for j in range(max):
        create_def(j)
        create_test_def(j)
