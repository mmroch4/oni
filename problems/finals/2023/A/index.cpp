#include <bits/stdc++.h>

using namespace std;

int main() {
  int n, v;

  cin >> n;
  
  vector<int> values(n);

  for (int i = 0; i < n; i++) {
    cin >> v;

    values[i] = v;
  }
  
  stable_sort(values.begin(), values.end());

  for (int i = 0; i < n; i++) {
    if (i == n - 1) continue;

    if (values[i] + 1 == values[i + 1]) {
      int b = values[i];
      values[i] = values[i + 1];
      values[i + 1] = b;
    }
  }
  
  for (int i = 0; i < n; i++) {
    if (i == n - 1) {
      cout << values[i] << "\n";
      continue;
    }
    cout << values[i] << " ";
  }
}