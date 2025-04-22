#include <bits/stdc++.h>

using namespace std;

int fact(int n) {
  if (n <= 1) {
    return 1;
  }

  int acc = 1;

  for (int i = 2; i <= n; i++)
  {
    acc *= i;
  }

  return acc;
}

int main() {
  int p, n, v;
  vector<int> values;
  cin >> p >> n;

  for (int i = 0; i < n; i++)
  {
    cin >> v;

    values.push_back(v);
  }
  
  if (p == 1) {
    stable_sort(values.begin(), values.end());

    int counter = -1;
    int current = -1;

    int acc = 0;

    for (int i = 0; i < n; i++) {
      if (values[i] == current) {
        counter++;

        if (i == n - 1 && 2 <= counter) {
          acc += fact(counter) / (2 * fact(counter - 2));
        }

        continue;
      }

      if (2 <= counter) {
        acc += fact(counter) / (2 * fact(counter - 2));
      }

      counter = 1;
      current = values[i];
    }

    cout << acc << "\n";
  }
  else {
    int acc = n;

    for (int i = 0; i < n; i++)
    {
      /* code */
    }
    

    cout << acc << "\n";
  }
}