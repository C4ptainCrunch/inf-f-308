import sys

sys.path.insert(0, '/home/nikita/Code/delay/scraper')

import align
import numpy as np


def fixture_from_file(stream):
    return np.array([[0 if char == "□" else int(char) for char in line.strip()] for line in stream])


def test_fix1():
    data = align.load_from_file(open('fixtures/1.points'))
    expected = fixture_from_file(open("fixtures/1.solution"))

    res = align.align(data)

    if not np.array_equal(res, expected):
        print(res)
        print("---")
        print(expected)

        assert False
