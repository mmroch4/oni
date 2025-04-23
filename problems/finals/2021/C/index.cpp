#include <bits/stdc++.h>

using namespace std;

bool separate(int a, int g, vector<int> &groups, vector<vector<int>>& adj, vector<int>& visited) {
  if (visited[a]) {
    if (groups[a] != g) {
      return false;
    }

    return true;
  }
  else {
    visited[a] = 1;
    groups[a] = g;

    bool is_possible = true;
    int alt[2] = {1, 0};

    for (auto j : adj[a])
    {
      if (!separate(j, alt[g], groups, adj, visited)) {
        is_possible = false;
        break;
      }
    }
    
    return is_possible;
  }
}

int main() {
  int p, t, n, m;

  cin >> p >> t;

  while (t) {
    t--;

    cin >> n >> m;

    vector<vector<int>> adj(n);
    
    int a, b;

    for (int i = 0; i < m; i++)
    {
      cin >> a >> b;
      a--;
      b--;

      adj[a].push_back(b);
      adj[b].push_back(a);
    }

    vector<int> groups(n);
    vector<int> visited(n);

    bool is_possible = separate(0, 0, groups, adj, visited);

    if (is_possible) {
      cout << "sim" << "\n";
    }
    else {
      cout << "nao" << "\n";
    }
  }

}