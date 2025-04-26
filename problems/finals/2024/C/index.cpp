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

int get_required_skills_to_win(int player, int n, vector<int>& duels, vector<int>& skills) {
  int winner = duels[1];

  if (player == winner) {
    return skills[player];
  }

  int i = n + player;
  int k = i;
  int rival;
  int a = 0;

  vector<pair<int, int>> ranges;

  while (k > 1) {
    rival = duels[k + (k % 2 == 0 ? 1 : -1)];

    vector<pair<int, int>> winning_ranges = get_winning_ranges(rival, player, skills);
    
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
        return -1;
      }

      ranges = new_ranges;
    }

    k = floor(k / 2);
    a++;
  }

  return ranges[0].first;
}

int main() {
  int p, n, q, s;

  cin >> p >> n;

  vector<int> duels(2 * n);
  vector<int> skills(n);

  if (p == 3) 
  {
    cin >> q;
  }

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

  if (p == 1) {
    cout << duels[1] + 1 << "\n";
  }
  else if (p == 2) {
    for (int player = 0; player < n; player++) {
      cout << (player == 0 ? "" : " ") << get_required_skills_to_win(player, n, duels, skills);
    }
  
    cout << "\n";
  }
  else
  {
    char a;

    for (int i = 0; i < q; i++)
    {
      cin >> a;

    if (a == 'B') {
      int player;

      cin >> player;
      player--;

      cout << get_required_skills_to_win(player, n, duels, skills) << "\n";
    }
    else if (a == 'M') {
      int player, skill;

      cin >> player >> skill;
      player--;

      skills[player] = skill;

      int k = floor((player + n) / 2);

      while (k >= 1) {
        duels[k] = duel(duels[2 * k], duels[2 * k + 1], skills);

        k = floor(k / 2);
      }
    }
    else {
      cout << duels[1] + 1 << "\n";
    }
    }
  }
}