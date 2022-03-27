#!/usr/bin/env python3

def num(x):
    return x ** 2

def test_num():
    assert num(5) == 25

def test_num2():
    assert num(5) == 26
