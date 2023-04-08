#include <iostream>
#include <string>
using namespace std;

int main() {
  string s;

  getline(cin, s);

  int i = 0;

  const int len = s.length();

  while (i < len) {
    if (s[i] == '<') {
      string ans;

      ans += s[i];

      while (i + 1 < len && s[i + 1] == '<') {
        ans += s[i + 1];
        i++;
      }

      while (i + 2 < len && s[i + 1] == '-' && s[i + 2] != '>') {
        ans += s[i + 1];
        i++;
      }

      if (i + 2 == len && s[i + 1] == '-') {
        ans += '-';
        i++;
      }

      cout << ans << endl;
      i++;
    }

    if (s[i] == '-') {
      string ans;

      ans += s[i];

      while (i + 1 < len && s[i + 1] != '>') {
        ans += s[i + 1];
        i++;
      }

      while (i + 1 < len && s[i + 1] == '>') {
        ans += s[i + 1];
        i++;
      }

      cout << ans << endl;
      i++;
    }
  }
}
