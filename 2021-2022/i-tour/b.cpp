#include <iostream>
#include <vector>
using namespace std;


int main(int argc, char const *argv[])
{
    int n; cin >> n;
    vector<int> a(n+1);
    for (int i = 0; i <= n; i++) {
        cin >> a[i];
    }
    a.push_back(0);

    vector<int> ans;
    for (int i = n+1; i >= 1; i--) {
        ans.push_back(a[i-1] + a[i]);
    }
    
    cout << a[0] << ' ';
    for (int i = ans.size() - 1; i >= 0; i--) {
        cout << ans[i] << ' ';
    }
    cout << endl;
    return 0;
}
