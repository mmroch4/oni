#include <bits/stdc++.h>

using namespace std;
/**
 * 
 * def intersection(a, b):
  [a_start, a_end] = a
  [b_start, b_end] = b
  
  if a_start - b_end <= 0 and 0 <= a_end - b_start:    
    start = a_start if 0 <= a_start - b_start else b_start
    end = a_end if 0 <= b_end - a_end else b_end
    
    return [start, end]
  
  return False
 */

int get_required_skills_to_win(int a, int m, int *skills, vector<int> *confronts, int *lost_to) {
  vector<int> to_confront;

  for (auto c : confronts[a]) {
    to_confront.push_back(c);
  }

  while (to_confront.size() < m) {
    vector<int> to_add = confronts[to_confront.back()];
    
    for (int u = to_confront.size(); u < to_add.size(); u++) {
      to_confront.push_back(to_add[u]);
    }
  }

  vector<vector<int>> intervals[to_confront.size()];

  for (int z = 0; z < to_confront.size(); z++) {
    int skill = skills[to_confront[z]];

    vector<int> right, left;
    bool has_left = false;
    int s_r, e_r, s_l, e_l;

    if (a < to_confront[z]) {
      s_r = skill;
    } 
    else {
      s_r = skill + 1;
    }

    e_r = skill + 999;

    if (1000 <= skill) {
      has_left = true;
      s_l = 0;
      e_l = skill - 1000;
    }

    right.push_back(s_r);
    right.push_back(e_r);
    intervals[z].push_back(right);

    if (has_left) {
      left.push_back(s_l);
      left.push_back(e_l);
      intervals[z].push_back(left);
    }
  }


  for (auto g : intervals) {
    for (auto e : g) {

      cout << e[0] << " " << e[1] << "\n";
    }
  }
}

int duel(int a, int b, int *skills) {
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

int get_champion(int n, int m, int *skills, vector<int> *confronts, int *lost_to) {
  vector<int> competitors;

  for (int i = 0; i < n; i++) {
    competitors.push_back(i);
  }

  for (int i = 0; i < m; i++) {
    vector<int> new_competitors;
    int previous = -1;

    for (auto c : competitors) {
      if (previous == -1) {
        previous = c;
        continue;
      }

      int duel_winner = duel(previous, c, skills);

      confronts[previous].push_back(c);
      confronts[c].push_back(previous);

      if (duel_winner == previous) {
        lost_to[c] = previous;
      } else {
        lost_to[previous] = c;
      }

      new_competitors.push_back(duel_winner);

      previous = -1;
    }
    
    competitors = new_competitors;
  }
  
  return competitors[0];
}

int main() {
  int p, n, s;

  cin >> p >> n;

  int skills[n];
  int lost_to[n];
  vector<int> confronts[n];
  int m = (int)log2(n);


  for (int i = 0; i < n; i++) {
    cin >> s;

    skills[i] = s;
    lost_to[i] = -1;
  }

  if (p == 1) {
    int champion = get_champion(n, m, skills, confronts, lost_to);

    cout << champion + 1 << "\n";
  }
  else if (p == 2) {
    int champion = get_champion(n, m, skills, confronts, lost_to);

    int required_skills_to_win[n];

    for (int i = 0; i < n; i++) {
      // if (i == champion) {
      //   required_skills_to_win[i] = skills[champion];
      //   continue;
      // }

      //required_skills_to_win[i] =
      if (i != 1) continue;
      get_required_skills_to_win(i, m, skills, confronts, lost_to);
    }
    
  }
}