#include <pybind11/pybind11.h>
#include <cppsub.hpp>
#include <cppadd.hpp>
//#include <cppmult.hpp>

PYBIND11_MODULE(pybind11_example, m) {
    m.doc() = "pybind11 example plugin"; // Optional module docstring
    m.def("cpp_add", &cppadd, "A function which multiplies two numbers");
    m.def("cpp_sub", &cppsub, "A function which substract two numbers");
}