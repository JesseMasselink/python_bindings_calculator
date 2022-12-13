#include <iostream>
#include <iomanip>
#include <cmath>
#include "cppfunc.hpp"

float cppadd(float int_param, float float_param) {
    float return_value = int_param + float_param;
//    std::cout << std::setprecision(1) << std::fixed
//	          << "    In cppmul: int " << int_param
//	          << " float " <<  float_param
//	          << " returning  " << return_value
//	          << std::endl;
    return return_value;
}

float cppsub(float int_param, float float_param) {
    float return_value = int_param - float_param;
//    std::cout << std::setprecision(1) << std::fixed
//	          << "    In cppmul: int " << int_param
//	          << " float " <<  float_param
//	          << " returning  " << return_value
//	          << std::endl;
    return return_value;
}

float cppmult(float int_param, float float_param) {
    float return_value = int_param * float_param;
//    std::cout << std::setprecision(1) << std::fixed
//	          << "    In cppmul: int " << int_param
//	          << " float " <<  float_param
//	          << " returning  " << return_value
//	          << std::endl;
    return return_value;
}

float cppdiv(float int_param, float float_param) {
    float return_value = int_param / float_param;
//    std::cout << std::setprecision(1) << std::fixed
//	          << "    In cppmul: int " << int_param
//	          << " float " <<  float_param
//	          << " returning  " << return_value
//	          << std::endl;
    return return_value;
}

float cppsquare(float int_param) {
    float return_value = int_param * int_param;
//    std::cout << std::setprecision(1) << std::fixed
//	          << "    In cppmul: int " << int_param
//	          << " float " <<  float_param
//	          << " returning  " << return_value
//	          << std::endl;
    return return_value;
}

float cppsqrt(float int_param) {
    float return_value = sqrt(int_param);
//    std::cout << std::setprecision(1) << std::fixed
//	          << "    In cppmul: int " << int_param
//	          << " float " <<  float_param
//	          << " returning  " << return_value
//	          << std::endl;
    return return_value;
}

int cppfib(int n){
auto start = high_resolution_clock::now();
    if (n <= 1)
        return n;
    return cppfib(n - 1) + cppfib(n - 2);
}