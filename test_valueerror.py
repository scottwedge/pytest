#!/usr/bin/env python3

import pytest

def rve():
    raise ValueError()


def test_rve():
    with pytest.raises(ValueError):
        rve()
