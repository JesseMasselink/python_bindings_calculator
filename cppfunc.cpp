#include <iostream>
#include <iomanip>
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

float cppdev(float int_param, float float_param) {
    float return_value = int_param / float_param;
//    std::cout << std::setprecision(1) << std::fixed
//	          << "    In cppmul: int " << int_param
//	          << " float " <<  float_param
//	          << " returning  " << return_value
//	          << std::endl;
    return return_value;
}