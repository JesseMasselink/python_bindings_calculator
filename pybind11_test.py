#!/usr/bin/env python
import pybind11_example

if __name__ == "__main__":
    # Sample data for our call:
    x, y = 6.5, 2.3

    answer = pybind11_example.cpp_function(x, y)
    answer_1 = pybind11_example.cpp_sub(x, y)
    print(f"    In Python: int: {x} float {y:.1f} return val {answer:.1f}")
    print(f"    In Python: int: {x} float {y:.1f} return val {answer_1:.1f}")
