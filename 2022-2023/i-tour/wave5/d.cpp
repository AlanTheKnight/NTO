#include <bits/stdc++.h>
using namespace std;

int len;

pair<int, int> get_dist(int a, int b) {
  bool r = b > a;
  int x = max(a, b), y = min(a, b);
  int d1 = len - x - 1 + y, d2 = x - y - 1;
  if (r) return {d1, d2};
  return {d2, d1};
}

int get_min_dist(int a, int b) {
  int x = max(a, b), y = min(a, b);
  int d1 = len - x - 1 + y, d2 = x - y - 1;
  return min(d1, d2);
}

int main() {
  string s;
  getline(cin, s);

  len = s.size();

  vector<int> chips;
  for (int i = 0; i < len; i++) {
    if (s[i] == '*') chips.push_back(i);
  }

  pair<int, int> min_sel = {INT_MAX, -1};
  for (auto sel : chips) {
    int rs = 0;
    for (auto x : chips) {
      if (x != sel) rs += get_min_dist(sel, x);
    }
    if (rs < min_sel.first) min_sel = make_pair(rs, sel);

    cout << sel << ' ' << rs << endl;
  }

  vector<pair<int, int>> left;
  left.reserve(len - 1);

  for (auto x : chips) {
    if (x != min_sel.second) {
      left.push_back({get_min_dist(min_sel.second, x), x});
    }
  }

  sort(left.begin(), left.end());

  pair<int, int> cur = {min_sel.second, min_sel.second};

  int ans = 0;

  for (auto &x : left) {
    int dlb = get_dist(cur.first, x.second).second;
    int drb = get_dist(cur.second, x.second).first;

    ans += min(drb, dlb);

    if (drb < dlb)
      cur.second--;
    else
      cur.first++;
  }

  cout << ans << endl;
}
