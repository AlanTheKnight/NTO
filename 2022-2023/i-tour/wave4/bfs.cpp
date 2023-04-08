#include <bits/stdc++.h>
#define INF 1000000
using namespace std;

int main(int argc, char const *argv[])
{
    int n;
    cin >> n;
    n++;

    int a;
    cin >> a;

    int s, t;
    cin >> s >> t;
    s--; t--;

    vector<int> dist(n, INF);
    vector<int> prev(n, -1);
    queue<int> q;

    for (int i = a; i <= 2 * a; i++)
    dist[s] = 0;
    q.push(s);

    while (!q.empty())
    {
        int u = q.front();
        q.pop();
        for (int to = 0; to < n; to++)
        {
            if (dist[to] > dist[u] + 1) {
                dist[to] = dist[u] + 1;
                prev[to] = u;
                q.push(to);
            }
        }
    }

    if (dist[t] == INF) {
        cout << -1 << endl;
    } else {
        cout << dist[t] << endl;
        if (dist[t] == 0) return 0;
        vector<int> path;
        int u = t;
        while (prev[u] != -1) {
            path.push_back(u + 1);
            u = prev[u];
        }
        path.push_back(s + 1);
        for (int i = path.size() - 1; i >= 0; i--) {
            cout << path[i] << " ";
        }
        cout << endl;
    }

    return 0;
}