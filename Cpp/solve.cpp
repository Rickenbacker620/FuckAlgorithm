#include <iostream>
#include <deque>
#ifdef DEBUG
#include "solve.hpp"
#else
#define INITIALIZE
#define FINALIZE
#endif

using namespace std;

int N, M;
int arr[4][3];
int cache[20];

int dfs(int n)
{
    auto &cb = cache[n];
    if (cb)
        return cb;
    if (n == 1)
        cb = 1;
    else if (n == 2)
        cb = 2;
    else
        cb = dfs(n - 1) + dfs(n - 2);
    return cb;
}

int main()
{
    INITIALIZE

    int res = dfs(10);
    cout << res;

    FINALIZE
}