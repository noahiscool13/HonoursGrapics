#include <pybind11/pybind11.h>
namespace py = pybind11;

long slowFuncCpp() {
    long a = 0;
    for (int i = 0;i<10000000;i++){
        a+=i;
    }
    return a;
}

PYBIND11_MODULE(example, m) {
m.doc() = "pybind11 example plugin"; // optional module docstring

m.def("slowFuncCpp", &slowFuncCpp, "A function which adds two numbers");
}