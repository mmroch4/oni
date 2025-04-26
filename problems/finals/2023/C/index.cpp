#include <bits/stdc++.h>

using namespace std;

int test(int l, int r, vector<vector<int>>& shields, vector<vector<int>>& memo) {
  if (memo[l][r] != -1)
  {
    return memo[l][r];
  }

  if (l == r - 1)
  {
    return shields[l][r];
  }

  int acc = 0;

  for (int i = l + 1; i < r; i++)
  {
    acc = max(acc, test(l, i, shields, memo) + test(i, r, shields, memo));
  }

  acc += shields[l][r];

  memo[l][r] = acc;
  memo[r][l] = acc;
  
  return acc;
}

int main() {
  int p, t, n, m, a, b;

  cin >> p >> t;

  while (t)
  {
    t--;

    cin >> n >> m;
    
    vector<vector<int>> shields(n, vector<int>(n));
    
    vector<vector<int>> memo(n, vector<int>(n, -1));
    
    for (int i = 0; i < m; i++)
    {
      cin >> a >> b;
      a--;
      b--;
      
      shields[a][b] = 1;
      shields[b][a] = 1;
    }
    
    cout << test(0, n - 1, shields, memo) << "\n";
  }
}