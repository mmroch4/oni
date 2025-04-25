#include <bits/stdc++.h>

using namespace std;

pair<bool, pair<int, int>> intersection(pair<int, int> a, pair<int, int> b) {
  if (a.first - b.second <= 0 && 0 <= a.second - b.first)
  {
    int s = 0 <= a.first - b.first ? a.first : b.first;
    int e = 0 <= b.second - a.second ? a.second : b.second;
    
    return {true, {s, e}};
  }   
  
  return {false, {-1, -1}};
}

vector<pair<int, int>> get_winning_ranges(int a, int b, vector<int>& skills) {
  pair<int, int> l, r;

  r = {a == b ? skills[a] : skills[a] + 1, skills[a] + 999};

  if (skills[a] < 1000) 
  {
    return {r};
  }

  l = {0, skills[a] - 1000};

  return {l, r};
}

int duel(int a, int b, vector<int>& skills) {
  int diff = abs(skills[a] - skills[b]);

  if (diff == 0) {
    return min(a, b);
  }
  else if (1000 <= diff) {
    if (skills[a] < skills[b]) {
      return a;
    } 
    else {
      return b;
    }
  } else {
    if (skills[a] < skills[b]) {
      return b;
    } 
    else {
      return a;
    }
  }
}

int main() {
  int p, n, s;

  cin >> p >> n;

  vector<int> duels(2 * n);
  vector<int> skills(n);

  for (int i = 0; i < n; i++)
  {
    cin >> s;

    duels[n + i] = i;
    skills[i] = s;
  }

  for (int u = n - 1; u > 0; u--)
  {
    duels[u] = duel(duels[2 * u], duels[2 * u + 1], skills);
  }

  if (p == 1) 
  {
    cout << duels[1] + 1 << "\n";
  }
  else if (p == 2) 
  {
    int winner = duels[1];

    for (int p = 0; p < n; p++)
    {
      if (p == winner) 
      {
        cout << (p != 0 ? " ": "") << skills[p];
        continue;
      }

      int i = n + p;
      int k = i;
      int rival;
      int a = 0;
      bool is_possible = true;

      vector<pair<int, int>> ranges;

      while (k > 1) {
        rival = duels[k + (k % 2 == 0 ? 1 : -1)];

        vector<pair<int, int>> winning_ranges = get_winning_ranges(rival, p, skills);
        
        if (a == 0)
        {
          for (auto r : winning_ranges)
          {
            ranges.push_back(r);
          }
        }
        else {
          vector<pair<int, int>> new_ranges;

          for (auto w : ranges)
          {
            for (auto z : winning_ranges) 
            {
              auto intersects = intersection(w, z);

              if (intersects.first) {
                new_ranges.push_back(intersects.second);
              }
            }
          }

          if (new_ranges.size() == 0) {
            is_possible = false;
            break;
          }

          ranges = new_ranges;
        }

        k = floor(k / 2);
        a++;
      }
    
      if (is_possible) 
      {
        cout << (p != 0 ? " ": "") << ranges[0].first;
      }
      else 
      {
        cout << (p != 0 ? " ": "") << -1;
      }
    }
  
    cout << "\n";
  }
}