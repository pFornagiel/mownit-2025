#include <iostream>
#include <fstream>
#include <cfloat>
#include <cmath>
#include <functional>
#include <type_traits>
#include <sstream>
#include <iomanip>

using namespace std;

// Mathematical functions
template <typename T>
T f(T x) {
    return sin(x) + cos(3*x);
}

template <typename T>
T real_derivative(T x) {
    return cos(x) - 3*sin(3*x);
}

template<typename T>
T derivative(T x, T h, std::function<T(T)> f) {
    return (f(x + h) - f(x)) / h;
}

// File operations
bool openOutputFile(std::ofstream& file, const std::string& filename) {
    file.open(filename);
    if (!file) {
        std::cerr << "Error opening file: " << filename << "\n";
        return false;
    }
    return true;
}

void typeInfoToFile() {
    std::ofstream file;
    if (!openOutputFile(file, "type_info.txt")) return;

    // Helper lambda to write type properties
    auto writeTypeProperties = [&file](const std::string& typeName, auto size, auto dig, 
                                     auto min, auto max, auto epsilon) {
        file << typeName << " Properties:\n"
             << "  Size: " << size << " bytes\n"
             << "  Precision (decimal digits): " << dig << "\n"
             << "  Min: " << min << "\n"
             << "  Max: " << max << "\n"
             << "  Epsilon: " << epsilon << "\n\n";
    };

    writeTypeProperties("Float", sizeof(float), FLT_DIG, FLT_MIN, FLT_MAX, FLT_EPSILON);
    writeTypeProperties("Double", sizeof(double), DBL_DIG, DBL_MIN, DBL_MAX, DBL_EPSILON);
    writeTypeProperties("Long Double", sizeof(long double), LDBL_DIG, LDBL_MIN, LDBL_MAX, LDBL_EPSILON);

    cout << "Type information written to 'type_info.txt'.\n";
}

void test_precisions() {
    std::ofstream data_file, oneplus_file, actual_file;
    if (!openOutputFile(data_file, "data.csv") || 
        !openOutputFile(oneplus_file, "oneplus.csv") || 
        !openOutputFile(actual_file, "actual.txt")) return;

    data_file << "i;h;float;double;long double;float_error;double_error;long_double_error\n";
    oneplus_file << "i;h;float;double;long double;error float\n";

    data_file << std::setprecision(20);
    oneplus_file << std::setprecision(20);
    actual_file << std::setprecision(20);

    for(int i = 0; i <= 40; i++) {
        const float h_float = pow(2.0f, -i);
        const double h_double = pow(2.0, -i);
        const long double h_long_double = pow(2.0L, -i);
        const int x = 1;

        // Calculate derivatives and errors
        auto [approx_float, approx_double, approx_long_double] = std::tuple{
            derivative<float>(x, h_float, f<float>),
            derivative<double>(x, h_double, f<double>),
            derivative<long double>(x, h_long_double, f<long double>)
        };

        auto [exact_float, exact_double, exact_long_double] = std::tuple{
            real_derivative<float>(x),
            real_derivative<double>(x),
            real_derivative<long double>(x)
        };

        auto [error_float, error_double, error_long_double] = std::tuple{
            fabs(approx_float - exact_float),
            fabs(approx_double - exact_double),
            fabs(approx_long_double - exact_long_double)
        };

        data_file << i << ";" << h_long_double 
                 << ";" << approx_float 
                 << ";" << approx_double 
                 << ";" << approx_long_double
                 << ";" << error_float
                 << ";" << error_double
                 << ";" << error_long_double << "\n";

        oneplus_file << i << ";" << h_long_double 
                    << ";" << (float)1 + h_float 
                    << ";" << (double)1 + h_double
                    << ";" << (long double)1 + h_long_double
                    << ";" << ((1 + h_long_double) - (1 + h_float)) << "\n";
    }

    actual_file << real_derivative<float>(1) << "\n"
                << real_derivative<double>(1) << "\n"
                << real_derivative<long double>(1) << "\n";
}

int main() {
    typeInfoToFile();
    test_precisions();
    return 0;
}

