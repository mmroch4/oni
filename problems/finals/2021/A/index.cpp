#include <bits/stdc++.h>

using namespace std;

bool descending_order(pair<int, int> a, pair<int, int> b) {
  return b.first < a.first;
}

int main() {
  int p, n, v;
  vector<int> mountains;
  
  cin >> p >> n;
  
  for (int i = 0; i < n; i++)
  {
    cin >> v;

    mountains.push_back(v);
  }

  if (p == 1) 
  {
    sort(mountains.begin(), mountains.end());
    
    int counter = 1;
    int acc = 0;
    
    for (int i = 1; i < n; i++)
    {
      if (mountains[i] == mountains[i - 1]) {
        acc += counter;
        counter++;
      }
      else {
        counter = 1;
      }
    }
    
    cout << acc << "\n";
  }
  else 
  {
    vector<pair<int, int>> indexed_mountains;

    for (int i = 0; i < n; i++) 
    {
      indexed_mountains.push_back({mountains[i], i});
    }
    
    sort(indexed_mountains.begin(), indexed_mountains.end(), descending_order);

    unordered_set<int> exclude;

    int acc = n;
    int max_range = 1;

    for (int i = 0; i < n; i++)
    {
      int global_index = indexed_mountains[i].second;

      exclude.insert(global_index);

      int r, l;
      r = l = global_index;

      while (1)
      {
        r++;
        l--;

        if (0 <= l && r < n && exclude.count(l) == 0 && exclude.count(r) == 0 && mountains[l] < indexed_mountains[i].first && mountains[r] < indexed_mountains[i].first) 
        {
          acc++;
        }
        else 
        {
          l++;
          r--;

          max_range = max(max_range, r - l + 1);
          break;
        }
      }
    }
    
    cout << max_range << " " << acc << "\n";
  }
}