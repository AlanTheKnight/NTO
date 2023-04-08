#include <iostream>
using namespace std;

int main()
{
    float p, b, c;
    cin >> p;
    b = p * 0.08;
    if (b > 100)
        b = 100;
    c = p * 0.05;
    cout << max(b, c) << endl;
    return 0;
}