#include <pybind11/pybind11.h>
//#include <cppadd.hpp>
//#include <cppsub.hpp>
//#include <cppmult.hpp>
#include <cppfib.hpp>
//#include <cppfunc.hpp>

PYBIND11_MODULE(pybind11_example, m) {
//    m.doc() = "pybind11 example plugin"; // Optional module docstring
//    m.def("cpp_add", &cppadd, "A function which adds two numbers");
//    m.def("cpp_sub", &cppsub, "A function which subtracts two numbers");
//    m.def("cpp_mult",&cppmult, "A function which multiplies two numbers");
//    m.def("cpp_div",&cppdiv, "A function which devides two numbers");
//    m.def("cpp_square",&cppsquare, "A function which multiplies a number by itself");
//    m.def("cpp_sqrt",&cppsqrt, "A function which finds the square root of a number");
    m.def("cpp_fib",&cppfib, "A function which finds the square root of a number");
}