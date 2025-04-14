#include <bits/stdc++.h>

using namespace std;

int main() {
  int p, n, k;

  cin >> p;
  cin >> n >> k;

  vector<int> cards(n);

  for (int i = 0; i < n; i++) { 
    cards[i] = i + 1;
  }
  
  if (p == 1) {
    for (int i = 0; i < k; i++) {
      int a, b, backup;

      cin >> a >> b;

      --a;
      --b;

      backup = cards[a];

      cards[a] = cards[b];
      cards[b] = backup;
    }
  } 
  else {
    for (int i = 0; i < k; i++) {
      int x;

      cin >> x;

      vector<int> updated_cards;

      for (int u = 0; u < x; u++) {
        updated_cards.push_back(cards[u]);
        updated_cards.push_back(cards[u + x]);
      }

      for (int u = 2 * x; u < n; u++) {
        updated_cards.push_back(cards[u]);
      }
      
      cards = updated_cards;
    }
  }

  for (int i = 0; i < n; i++) {
    cout << cards[i] << "\n";
  }

  return 0;
}