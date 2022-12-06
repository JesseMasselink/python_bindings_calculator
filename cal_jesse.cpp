#include <pybind11/pybind11.h>

// function
float add(float arg1, float arg2){
    return arg1 + arg2;
}
// wrapper
PYBIND11_MODULE(pybind11_add_module m){
    m.doc() = "pybind11 test function"; // optionele docstring
    m.def("cpp_add_function", &add, "A function that adds two numbers");
}

// function
float multiply(float arg1, float arg2){
    return arg1 * arg2;
}
// wrapper
PYBIND11_MODULE(pybind11_multiply_module, m){
    m.doc() = "pybind11 multiply function"; // optionele docstring
    m.def("cpp_multiply_function", &multiply, "A function that adds two numbers");
}