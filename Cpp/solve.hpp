#include <fstream>

#define cin input

#define INITIALIZE ifstream input("input");
#define FINALIZE cout << endl;

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
