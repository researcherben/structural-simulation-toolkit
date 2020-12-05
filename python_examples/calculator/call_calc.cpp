#include <iostream>
#include <pybind11/embed.h>

namespace py = pybind11;


int main() {
    std::cout << "Hello World!";

    // https://pybind11.readthedocs.io/en/stable/advanced/embedding.html
    py::module_ calc = py::module_::import("calc");
    py::object result = calc.attr("add")(1, 2);
    int n = result.cast<int>();
    assert(n == 3);

    return 0;
}
