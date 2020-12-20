#include <pybind11/embed.h>
namespace py = pybind11;

// from https://pybind11.readthedocs.io/en/stable/advanced/embedding.html#executing-python-code

int main() {
    py::scoped_interpreter guard{};

    py::exec(R"(
        kwargs = dict(name="World", number=42)
        message = "Hello, {name}! The answer is {number}".format(**kwargs)
        print(message)
    )");
}

