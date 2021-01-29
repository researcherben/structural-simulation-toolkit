#include <pybind11/embed.h> // everything needed for embedding
namespace py = pybind11;

// from https://pybind11.readthedocs.io/en/stable/advanced/embedding.html#getting-started

int main() {
    py::scoped_interpreter guard{}; // start the interpreter and keep it alive

    py::print("Hello, World!"); // use the Python API
}
