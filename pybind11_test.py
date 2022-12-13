#!/usr/bin/env python
import pybind11_example
import timeit

# def py_fibo(n):
#    if n <= 1:
#        return n
#    else:
#        return(py_fibo(n-1) + py_fibo(n-2))

if __name__ == "__main__":
    # Sample data for our call:
    x, y = 6.5, 2.3
    i = 10

    # answer   = pybind11_example.cpp_add(x, y)
    # answer_1 = pybind11_example.cpp_sub(x, y)
    # answer_2 = pybind11_example.cpp_mult(x, y)
    # answer_3 = pybind11_example.cpp_div(x, y)
    # answer_4 = pybind11_example.cpp_square(x)
    # answer_5 = pybind11_example.cpp_sqrt(x)
    start = timeit.default_timer()
    fib = pybind11_example.cpp_fib(i)
    stop = timeit.default_timer()
    start_1 = timeit.default_timer()
    # py_fib = py_fibo(i)
    stop_1 = timeit.default_timer()
    # print(f"    In Python: int: {x} added to float {y:.1f} return val {answer:.1f}")
    # print(f"    In Python: int: {x} with subtracted float {y:.1f} return val {answer_1:.1f}")
    # print(f"    In Python: int: {x} multiplied by float {y:.1f} return val {answer_2:.1f}")
    # print(f"    In Python: int: {x} devided by float {y:.1f} return val {answer_3:.1f}")
    # print(f"    In Python: int: {x} multiplied by float {x:.1f} return val {answer_4:.1f}")
    # print(f"    In Python: int: {x}'s root is return val {answer_5:.1f}")
    print(f"    In C++: int: {i}'s fibbionacci sequence value is {fib} and it takes {stop - start} seconds")
    print(f"    In Python: int: {i}'s fibbionacci sequence value is {fib} and it takes {stop_1 - start_1} seconds")