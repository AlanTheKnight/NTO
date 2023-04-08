#include <iostream>
#include <vector>
#include <set>
using namespace std;

const int INF = 10000000;

void printVector(vector<int> vec)
{
    for (auto i : vec)
        cout << i << ' ';
    cout << endl;
}

int main()
{
    freopen("output.txt", "w", stdout);

    int n, a;
    cin >> a >> n;

    const int MONEY_COUNT = 2 * a - a + 1;
    const int MONEY_SUM = ((a + 2 * a) * MONEY_COUNT) / 2;

    printf("Count: %d; Sum: %d\n", MONEY_COUNT, MONEY_SUM);

    vector<vector<int>> A(MONEY_COUNT + 1, vector<int>(n + 1, false));

    vector<int> w(MONEY_COUNT + 1);
    for (int i = a; i <= 2 * a; i++) {
        w[i - a + 1] = i;
    }

    printf("Money: "); printVector(w);

    for (int k = 1; k <= MONEY_COUNT; k++) {
        for (int s = 1; s <= n; s++) {
            if (s >= w[k]) {
                A[k][s] = max(A[k - 1][s], A[k - 1][s - w[k]] + 1);
            } else {
                A[k][s] = A[k - 1][s];
            }
        }
    }

    for (auto row : A) {
        for (auto i : row) {
            cout << i << ' ';
        }
        cout << endl;
    }

    int k = MONEY_COUNT;
    set<int> ans;
    for (int i = n; i > 1; i--) {
        if (A[i][k] != A[i - 1][k]){
            ans.insert(w[i]);
            k -= w[i];
        }
    }


    for (auto c : ans)
        cout << c << ' ';
    cout << endl;
}
