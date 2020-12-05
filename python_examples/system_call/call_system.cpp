#include <iostream>
#include <cstdlib>

using namespace std;

int main ()
{

    string num1_str;
    string num2_str;

    cout << "number to add: ";
    getline(cin, num1_str);

    cout << "second number to add: ";
    getline(cin, num2_str);

    // https://stackoverflow.com/a/26106662/1164295
    int result = system(("/usr/bin/python3 calc.py "+num1_str+" "+num2_str).c_str());
    cout << (num1_str+"+"+num2_str+"=") << result << endl;

    return 0;
}
