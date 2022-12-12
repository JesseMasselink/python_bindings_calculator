#ifdef _MSC_VER
    #define EXPORT_SYMBOL __declspec(dllexport)
#else
    #define EXPORT_SYMBOL
#endif

#ifdef __cplusplus
extern "C" {
#endif

EXPORT_SYMBOL float cppadd(float int_param, float float_param);
EXPORT_SYMBOL float cppsub(float int_param, float float_param);
EXPORT_SYMBOL float cppmult(float int_param, float float_param);
EXPORT_SYMBOL float cppdiv(float int_param, float float_param);
EXPORT_SYMBOL float cppsquare(float int_param);
EXPORT_SYMBOL float cppsqrt(float int_param);
EXPORT_SYMBOL int cppfib(int int_param);

#ifdef __cplusplus
}
#endif