#include <bits/stdc++.h>

using namespace std;

bool descending_order(pair<int, int> a, pair<int, int> b) {
  return b.first < a.first;
}

int main() {
  int p, n, v;
  
  cin >> p >> n;
  
  if (p == 1) 
  {
    vector<int> mountains;

    for (int i = 0; i < n; i++)
    {
      cin >> v;
  
      mountains.push_back(v);
    }

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
      cin >> v;
  
      indexed_mountains.push_back({v, i});
    }
    
    sort(indexed_mountains.begin(), indexed_mountains.end(), descending_order);

    unordered_set<int> exclude;

    int acc = n;
    int max_range = 1;

    for (int i = 0; i < n; i++)
    {
      int global_index = indexed_mountains[i].second;

      // cout << " ------------- NUM: " << indexed_mountains[i].first << "---------------- \n";
      
      if (i == 0) 
      {
        // cout << "-- BIGGEST -- " << indexed_mountains[i].first << " " << indexed_mountains[i].second << "\n";
        // cout << "before acc: " << acc << "\n";
        int p = min(global_index, n - 1 - global_index);
        acc += p;
        max_range = max(max_range, p * 2 + 1);
        // cout << "after acc: " << acc << "\n";
        exclude.insert(global_index);
        continue;
      }

      int r, l;
      r = l = global_index;

      bool stop = false;

      while (!stop)
      {
        r++;
        l--;

        if (0 <= l && r < n && exclude.count(l) == 0 && exclude.count(r) == 0) 
        {
          // cout << "range: " << l << " " << r << "\n";
          // cout << "before acc: " << acc << "\n";
          acc++;
          // cout << "after acc: " << acc << "\n";
          continue;
        }
        else 
        {
          // cout << "impossible range " << l << " " << r << "\n";
          l++;
          r--;

          max_range = max(max_range, r - l + 1);
          stop = true;
          break;
        }
      }
      
      exclude.insert(global_index);
    }
    
    cout << max_range << " " << acc << "\n";
  }
}
