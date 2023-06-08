#include <iostream>
#ifdef DEBUG
#include "solve.hpp"
#else
#define INITIALIZE
#define FINALIZE
#endif

using namespace std;

int n[2][3];

int main()
{
    INITIALIZE

    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            cin >> n[i][j];
        }
    }
    FORM(n, 1, 2);

    FINALIZE
}