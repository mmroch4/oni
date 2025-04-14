#include <bits/stdc++.h>

using namespace std;

int main() {
  int p, n;
  long long acc, m, f;
  vector<int> reps;
  
  cin >> p >> n;

  cin >> f;

  acc = m = f;

  for (int i = 1; i < n; i++) {
    long long a;

    cin >> a;

    acc = max(a, acc + a);

    if (m < acc) {
      m = acc;
    }
  }

  cout << m << "\n";
}