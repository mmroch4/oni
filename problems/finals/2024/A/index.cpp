#include <bits/stdc++.h>

using namespace std;

int main() {
  int p, n, v, d, s, last_value;
  vector<int> b, c;

  cin >> p >> n;

  if (p == 1) {
    for (int i = 0; i < n; i++) {
      cin >> v;
      
      d = 2 * v; // double
      s = -v; // symmetric
      
      if (v == 0) {
        b.push_back(1);
        c.push_back(-1);
      } else if (v < 0) {
        b.push_back(s);
        c.push_back(d);
      } else {
        b.push_back(d);
        c.push_back(s);
      }
    }
  } else {
    int diff;

    
    cin >> v;
    last_value = v;

    d = 2 * v; // double
    s = -v; // symmetric

    if (v == 0) {
      b.push_back(1);
      c.push_back(-1);
    } else if (v < 0) {
      b.push_back(s);
      c.push_back(d);
    } else {
      b.push_back(d);
      c.push_back(s);
    }

    for (int i = 1; i < n; i++) {
      cin >> v;

      diff = v - last_value;

      if (0 <= diff) {
        b.push_back(b[i - 1] + 1 + diff);
        c.push_back(c[i - 1] - 1);
      } else {
        b.push_back(b[i - 1] + 1);
        c.push_back(c[i - 1] - 1 + diff);
      }

      last_value = v;
    }
  }

  for (long long x : b) {
    cout << x << " ";
  }
  
  cout << "\n";
  
  for (long long x : c) {
    cout << x << " ";
  }
  
  cout << "\n";
}