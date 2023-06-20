#include <fstream>
#include <chrono>

#define cin input

#define INITIALIZE           \
    ifstream input("input"); \
    auto start_ = std::chrono::high_resolution_clock::now();

#define FINALIZE                                             \
    auto end_ = std::chrono::high_resolution_clock::now();   \
    std::chrono::duration<double> duration_ = end_ - start_; \
    std::cout << std::endl << "Runtime: " << duration_.count() << " seconds" << std::endl;

#define SEP cout << "-------------------------------------" << endl;
#define LOG(x) cout << #x << " = " << x << endl;

#define FORM(k, n, m)                    \
    for (int i = 0; i <= 2 * m + 2; i++) \
        cout << '+';                     \
    cout << endl;                        \
    for (int i = 0; i <= n; i++)         \
    {                                    \
        cout << '|';                     \
        for (int j = 0; j <= m; j++)     \
            cout << k[i][j] << '|';      \
        cout << endl;                    \
    }                                    \
    for (int i = 0; i <= 2 * m + 2; i++) \
        cout << '+';
