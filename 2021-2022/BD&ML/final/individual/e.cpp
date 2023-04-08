#include <bits/stdc++.h>
using namespace std;

#define pii pair<int, int>

bool isValid(pii coords, int height, int width) {
  return (coords.first >= 0 && coords.second >= 0 && coords.first < height &&
          coords.second < width);
}

int getDist(vector<vector<int>> &dist, pii coords) {
  return dist[coords.first][coords.second];
}

void setDist(vector<vector<int>> &dist, pii coords, int value) {
  dist[coords.first][coords.second] = value;
}

int main() {
  map<char, pair<int, int>> deltas;
  deltas['S'] = {1, 0};
  deltas['N'] = {-1, 0};
  deltas['W'] = {0, -1};
  deltas['E'] = {0, 1};

  int n, m;
  cin >> n >> m;
  vector<vector<char>> field(n, vector<char>(m));
  vector<vector<int>> dist(n, vector<int>(m, INT_MAX));

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) cin >> field[i][j];
  }

  set<pair<int, pii>> s;
  dist[0][0] = 0;
  s.insert({0, {0, 0}});

  while (!s.empty()) {
    auto cur = *s.begin();
    s.erase(s.begin());

    auto curCoords = cur.second;
    auto curDist = cur.first;

    // cout << "Cur " << curDist << ' ' << curCoords.first << ' '
    //      << curCoords.second << endl;

    auto booster_delta = deltas[field[curCoords.first][curCoords.second]];
    auto booster = make_pair(curCoords.first + booster_delta.first, curCoords.second + booster_delta.second);

    // We have a booster and the cell hasn't been visited yet
    if (isValid(booster, n, m)) {
      if (getDist(dist, booster) > curDist) {
        // cout << "Using booster " << field[curCoords.first][curCoords.second]
        //      << ' ' << booster.first << ' ' << booster.second << endl;
        s.erase({curDist, booster});
        setDist(dist, booster, curDist);
        s.insert({curDist, booster});
      }
    }

    int dy[] = {1, -1, 0, 0};
    int dx[] = {0, 0, 1, -1};

    for (int i = 0; i < 4; i++) {
      auto newCoord =
          make_pair(curCoords.first + dy[i], curCoords.second + dx[i]);

      if (isValid(newCoord, n, m)) {
        if (getDist(dist, newCoord) > curDist + 1) {
          s.erase({curDist + 1, newCoord});
          setDist(dist, newCoord, curDist + 1);
          s.insert({curDist + 1, newCoord});
        }
      }
    }
  }

  cout << dist[n - 1][m - 1] << endl;
}