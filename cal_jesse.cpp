#include <pybind11/pybind11.h>

// function
float add(float arg1, float arg2){
    return arg1 + arg2;
}
// wrapper
PYBIND11_MODULE(pybind11_add_module m){
    m.doc() = "pybind11 add function"; // optionele docstring
    m.def("cpp_add_function", &add, "A function that adds two numbers");
}

// function
float multiply(float arg1, float arg2){
    return arg1 * arg2;
}
// wrapper
PYBIND11_MODULE(pybind11_multiply_module, m){
    m.doc() = "pybind11 multiply function"; // optionele docstring
    m.def("cpp_multiply_function", &multiply, "A function that multiplies two numbers");
}

// function
float square(float arg1){
    return arg1 * arg1;
}
// wrapper
PYBIND11_MODULE(pybind11_square_module, m){
    m.doc() = "pybind11 square function"; // optionele docstring
    m.def("cpp_square_function", &square, "A function that gives back the argument squared");
}

unsigned int fibinacci(int n){
    if(n < 2){
        return n;
    }
    return fibinacci(n - 1) + fibinacci(n - 2);
}

PYBIND11_MODULE(pybind11_fibinacci_module, m) {
    m.def("fibinacci_cpp", &fibinacci, "Recursive fibinacci algorithm.");
}