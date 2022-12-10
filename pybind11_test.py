#!/usr/bin/env python
import pybind11_example

if __name__ == "__main__":
    # Sample data for our call:
    x, y = 6.5, 2.3

    answer   = pybind11_example.cpp_add(x, y)
    answer_1 = pybind11_example.cpp_sub(x, y)
    answer_2 = pybind11_example.cpp_mult(x, y)
    answer_3 = pybind11_example.cpp_dev(x, y)
    answer_4 = pybind11_example.cpp_square(x)
    answer_5 = pybind11_example.cpp_sqrt(x)
    print(f"    In Python: int: {x} added to float {y:.1f} return val {answer:.1f}")
    print(f"    In Python: int: {x} with subtracted float {y:.1f} return val {answer_1:.1f}")
    print(f"    In Python: int: {x} multiplied by float {y:.1f} return val {answer_2:.1f}")
    print(f"    In Python: int: {x} devided by float {y:.1f} return val {answer_3:.1f}")
    print(f"    In Python: int: {x} multiplied by float {x:.1f} return val {answer_4:.1f}")
    print(f"    In Python: int: {x}'s root is return val {answer_5:.1f}")